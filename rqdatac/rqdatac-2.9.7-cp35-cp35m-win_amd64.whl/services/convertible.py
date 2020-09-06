# -*- coding: utf-8 -*-
import warnings
import pandas as pd
from rqdatac.services.constant import RATETYPE_CN, RATECOMP_CN

from rqdatac.client import get_client
from rqdatac.validators import (
    ensure_int,
    ensure_date_int,
    ensure_order_book_id,
    ensure_order_book_ids,
    ensure_date_range,
    ensure_dates_base_on_listed_date,
    ensure_list_of_string, ensure_date_or_today_int, check_items_in_container)
from rqdatac.utils import to_datetime, int8_to_datetime
from rqdatac.decorators import export_as_api, ttl_cache
from rqdatac.services.calendar import (
    get_trading_dates,
)
from rqdatac.services import shenwan

INS_COLUMNS = [
    "order_book_id",
    "symbol",
    "full_name",
    "exchange",
    "bond_type",
    "trade_type",
    "value_date",
    "maturity_date",
    "par_value",
    "coupon_rate",
    "coupon_frequency",
    "coupon_method",
    "compensation_rate",
    "total_issue_size",
    "de_listed_date",
    "stock_code",
    "conversion_start_date",
    "conversion_end_date",
    "redemption_price",
    "issue_price",
    "call_protection",
    "listed_date"
]


class Instrument:
    def __init__(self, attrs):
        self.__dict__.update(attrs)
        self.__cache = {}

    def __str__(self):
        return "{}(\n{}\n)".format(
            type(self).__name__,
            ",\n".join(["{}={!r}".format(k, v) for k, v in self.items() if not k.startswith("_")]),
        )

    __repr__ = __str__

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def get(self, item, default=None):
        return self.__dict__.get(item, default)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def __cache_get(self, v):
        return self.__cache.get(v)

    def __cache_set(self, k, v):
        self.__cache[k] = v

    def coupon_rate_table(self):
        """变动利率可转债信息"""
        if "coupon_rate_table" in self.__cache:
            return self.__cache_get("coupon_rate_table")
        info = get_client().execute("convertible.get_coupon_rate_table", self.order_book_id)
        info = pd.DataFrame(info).set_index(['start_date', 'end_date']) if info else None
        self.__cache_set("coupon_rate_table", info)
        return info

    def option(self, option_type=None):
        if option_type is not None:
            option_type = ensure_int(option_type)
            if option_type not in (1, 2, 3, 4, 5, 6, 7):
                raise ValueError("option_type: expect value in (None, 1, 2, 3, 4, 5, 6, 7)")

        data = get_client().execute("convertible.option", self.order_book_id, option_type)
        if not data:
            return

        df = pd.DataFrame(data)
        if 'payment_year' in df.columns:
            sort_fields = ['option_type', 'payment_year']
        else:
            sort_fields = ['option_type']
        df = df.sort_values(sort_fields).reset_index()
        column_order = ['option_type', 'start_date', 'end_date', 'payment_year', 'level', 'window_days',
                        'reach_days', 'frequency', 'price', 'if_include_interest', 'remark']
        column = [i for i in column_order if i in df.columns]
        return df[column]


@ttl_cache(12 * 3600)
def _all_instruments_dict(market="cn"):
    return {
        i['order_book_id']: Instrument(i)
        for i in get_client().execute("convertible.all_instruments", market=market)
    }


@export_as_api(namespace="convertible")
def all_instruments(date=None, market="cn"):
    """获取所有可转债详细信息

    :param market:  (Default value = "cn")
    :returns: DataFrame
    """
    profile = lambda v: (
        v.order_book_id,
        v.symbol,
        v.full_name,
        v.exchange,
        v.bond_type,
        v.trade_type,
        v.value_date,
        v.maturity_date,
        v.par_value,
        v.coupon_rate,
        v.coupon_frequency,
        v.coupon_method,
        v.compensation_rate,
        v.total_issue_size,
        v.de_listed_date,
        v.stock_code,
        v.conversion_start_date,
        v.conversion_end_date,
        v.redemption_price,
        v.issue_price,
        v.call_protection,
        v.listed_date,
    )

    def judge(listed_date, de_listed_date):
        if listed_date and de_listed_date:
            return listed_date <= date and de_listed_date > date
        if listed_date:
            return listed_date <= date
        else:
            return False

    if date:
        date = to_datetime(date)
        data = [profile(v) for v in _all_instruments_dict(market).values() if judge(v.listed_date, v.de_listed_date)]
    else:
        data = [profile(v) for v in _all_instruments_dict(market).values()]
    df = pd.DataFrame(
        data,
        columns=INS_COLUMNS,
    )
    df.sort_values('order_book_id', inplace=True)
    return df.reset_index(drop=True)


@export_as_api(namespace="convertible")
def instruments(order_book_ids, market="cn"):
    """获取可转债详细信息

    :param order_book_ids: 可转债代码，str 或 list of str
    :param market:  (Default value = "cn")
    :returns: Instrument object or list of Instrument object
            取决于参数是一个 order_book_id 还是多个 order_book_id
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    all_dict = _all_instruments_dict(market)
    if len(order_book_ids) == 1:
        try:
            return all_dict[order_book_ids[0]]
        except KeyError:
            warnings.warn('unknown convertible order_book_id: {}'.format(order_book_ids))
            return
    all_list = (all_dict.get(i) for i in order_book_ids)
    return [i for i in all_list if i]


@export_as_api(namespace="convertible")
def get_cash_flow(order_book_ids, start_date=None, end_date=None, market="cn"):
    """获取现金流信息

    :param order_book_ids: 可转债ID str or list
    :param start_date: 开始日期，默认为None
    :param end_date: 结束日期，默认为None
    :param market:  (Default value = "cn")
    :return: pd.DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    if start_date:
        start_date = ensure_date_int(start_date)
    if end_date:
        end_date = ensure_date_int(end_date)
    data = get_client().execute("convertible.get_cash_flow", order_book_ids, start_date, end_date, market=market)
    if not data:
        return
    df = pd.DataFrame(data)
    df.set_index(["order_book_id", "payment_date"], inplace=True)
    return df


@export_as_api(namespace="convertible")
def get_call_info(order_book_ids, start_date=None, end_date=None, market="cn"):
    """获取赎回信息

    :param order_book_ids: 可转债ID，str or list
    :param start_date: 开始日期，默认为None
    :param end_date: 结束日期，默认为None
    :param market:  (Default value = "cn")
    :return: pd.DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    if start_date:
        start_date = ensure_date_int(start_date)
    if end_date:
        end_date = ensure_date_int(end_date)
    data = get_client().execute("convertible.get_call_info", order_book_ids, start_date, end_date, market=market)
    if not data:
        return
    df = pd.DataFrame(data)
    df.set_index(["order_book_id", "info_date"], inplace=True)
    return df


@export_as_api(namespace="convertible")
def get_put_info(order_book_ids, start_date=None, end_date=None, market="cn"):
    """获取回售信息

    :param order_book_ids: 可转债ID，str or list
    :param start_date: 开始日期，默认为None
    :param end_date: 结束日期，默认为None
    :param market:  (Default value = "cn")
    :return: pd.DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    if start_date:
        start_date = ensure_date_int(start_date)
    if end_date:
        end_date = ensure_date_int(end_date)
    data = get_client().execute("convertible.get_put_info", order_book_ids, start_date, end_date, market=market)
    if not data:
        return
    df = pd.DataFrame(data)
    df.set_index(["order_book_id", "info_date"], inplace=True)
    return df


@export_as_api(namespace="convertible")
def get_conversion_price(order_book_ids, start_date=None, end_date=None, market="cn"):
    """获取转股价变动信息

    :param order_book_ids: 可转债ID，str or list
    :param start_date: 开始日期，默认为None
    :param end_date: 结束日期，默认为None
    :param market:  (Default value = "cn")
    :return: pd.DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    if start_date:
        start_date = ensure_date_int(start_date)
    if end_date:
        end_date = ensure_date_int(end_date)
    data = get_client().execute("convertible.get_conversion_price", order_book_ids, start_date, end_date, market=market)
    if not data:
        return
    df = pd.DataFrame(data)
    df.set_index(["order_book_id", "info_date"], inplace=True)
    return df


@export_as_api(namespace="convertible")
def get_conversion_info(order_book_ids, start_date=None, end_date=None, market="cn"):
    """获取转股变动信息

    :param order_book_ids: 可转债ID，str or list
    :param start_date: 开始日期，默认为None
    :param end_date: 结束日期，默认为None
    :param market:  (Default value = "cn")
    :return: pd.DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    if start_date:
        start_date = ensure_date_int(start_date)
    if end_date:
        end_date = ensure_date_int(end_date)
    data = get_client().execute("convertible.get_conversion_info", order_book_ids, start_date, end_date, market=market)
    if not data:
        return
    df = pd.DataFrame(data)
    df.set_index(["order_book_id", "info_date"], inplace=True)
    return df


@export_as_api(namespace="convertible")
def is_suspended(order_book_ids, start_date=None, end_date=None):
    """获取停牌信息
    :param order_book_ids: 可转债ID
    :param start_date: 开始日期, 如'2013-01-04' (Default value = None)
    :param end_date: 结束日期，如'2014-01-04' (Default value = None)
    :returns: DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    if len(order_book_ids) == 1:
        instrument = instruments(order_book_ids[0], market="cn")
        start_date, end_date = ensure_dates_base_on_listed_date(instrument, start_date, end_date, "cn")
        if start_date is None:
            return
    start_date, end_date = ensure_date_range(start_date, end_date)

    trading_dates = pd.to_datetime(get_trading_dates(start_date, end_date, market="cn"))
    df = pd.DataFrame(data=False, columns=order_book_ids, index=trading_dates)
    data = get_client().execute("convertible.is_suspended", order_book_ids, start_date, end_date, market="cn")
    for (order_book_id, date) in data:
        date = to_datetime(date)
        df.at[date, order_book_id] = True
    return df


ISSUER_FIELDS = [
    'credit_date',
    'credit_level',
    'rating_type',
    'institution',
    'organization',
    'org_type',
    'outlook',
    'adjusted_direction',
]
DEBT_FIELDS = [
    'credit_date',
    'credit_level',
    'rating_type',
    'institution',
    'outlook',
    'adjusted_direction',
]


@export_as_api(namespace="convertible")
def get_credit_rating(order_book_ids, start_date=None, end_date=None, institution=None, target='debt', fields=None):
    """
    :param order_book_ids: bond id, str or str list
    :param start_date: start date, datatime, int or str
    :param end_date: end date, datatime, int or str
    :param institution: crediting company name
    :param target: 'debt' or 'issuer'
    :param fields: 筛选字段
            debt: [
                'credit_date','credit_level','rating_type','institution','outlook','adjusted_direction'
            ]
            issuer: [
                'credit_date','credit_level','rating_type','institution',
                'organization', 'org_type','outlook','adjusted_direction',
            ]
    :return: a pandas DataFrame with order_book_id as index
    """
    check_items_in_container(target, ['debt', 'issuer'], 'target')

    all_fields = DEBT_FIELDS if target == 'debt' else ISSUER_FIELDS
    fields = ensure_list_of_string(fields, "fields") if fields else all_fields
    order_book_ids = ensure_list_of_string(order_book_ids, "order_book_ids")
    start_date = ensure_date_int(start_date) if start_date is not None else start_date
    end_date = ensure_date_int(end_date) if end_date is not None else end_date

    data = get_client().execute(
        'convertible.get_credit_rating', order_book_ids, start_date, end_date, institution, target, fields
    )
    if not data:
        return
    df = pd.DataFrame(data)
    df.set_index(['order_book_id'], inplace=True)
    return df.reindex(columns=fields)


@export_as_api(namespace="convertible")
def rating(date=None, credit_level=None, institution=None, rating_type=None, target='debt'):
    """
    Get rating information for company or bond
    :param date: str, int, or datatime
        1): 存续债券的判定是date在[value_date,maturity_date]之间
        2): 控制credit_date返回当前最新的日期
    :param credit_level: eg: 'AAA'
    :param institution: rating company name
    :param rating_type: rating type name
    :param target: 'debt' or 'issuer'
    :return:
    """
    check_items_in_container(target, ['debt', 'issuer'], 'target')
    if institution is not None:
        check_items_in_container(institution, RATECOMP_CN, 'institution')
    if rating_type is not None:
        check_items_in_container(rating_type, RATETYPE_CN, 'rating_type')
    date = ensure_date_int(date) if date else None

    res = get_client().execute("convertible.rating", date, credit_level, institution, rating_type, target)

    if date and res and target == 'debt':
        ins = instruments(res)
        if not isinstance(ins, list):
            ins = [ins]
        res = [i.order_book_id for i in ins if i.value_date <= int8_to_datetime(date) <= i.maturity_date]
    return res


@export_as_api(namespace="convertible")
def get_latest_rating(order_book_ids, date, institution=None, rating_type=None, target='debt'):
    """
    获取在给定日期之前的最新评级记录.
    返回credit_date和参数date前差距时间最短的一条记录，无需返回所有评级机构最新记录

    :param order_book_ids: str or List[str]债券id列表
    :param date: str or int or datetime.date) 评级日期; 会返回该日期之前的最新评级记录.
    :param institution: str or List[str] or None 评级机构; 若为None, 则返回所有评级机构的最新记录
    :param rating_type: str or None 评级类型; 如果给定的话, 只返回该评级类型下最新的评级信息,
        如果设为None, 则不管评级类型, 直接返回最新评级记录
    :param target: str 评级类型, 可选值为 'debt'(代表债券评级) 或者 'issuer'(代表主体评级);
    :return: a pandas DataFrame with order_book_id as index.
    """
    order_book_ids = ensure_list_of_string(order_book_ids, "order_book_ids")
    check_items_in_container(target, ['debt', 'issuer'], 'target')
    if institution is not None:
        institution = ensure_list_of_string(institution, "institution")
        check_items_in_container(institution, RATECOMP_CN, 'institution')

    data = get_client().execute(
        "convertible.get_latest_rating",
        order_book_ids,
        ensure_date_int(date),
        institution,
        rating_type,
        target
    )
    if not data:
        return
    df = pd.DataFrame.from_records(data)
    df.sort_values(["order_book_id", "credit_date"], ascending=False, inplace=True)
    df.set_index("order_book_id", inplace=True)
    return df


@export_as_api(namespace="convertible")
def get_instrument_industry(order_book_ids, source='citics', level=1, date=None, market="cn"):
    """获取可转债对应的行业

    :param order_book_ids: 可转债order_book_id，如['000001.XSHE', '000002.XSHE']
    :param source: 分类来源。citics 以及 citics_2019: 中信, gildata: 聚源
    :param date: 如 '2015-01-07' (Default value = None)
    :param level:  (Default value = 1)
    :param market:  (Default value = "cn")
    :returns: DataFrame
        index: order_book_id
        columns:
            if level == 1: ["first_industry_code", "first_industry_name"]
            if level == 2: ["second_industry_code", "second_industry_name"]
            if level == 3: ["third_industry_code", "third_industry_name"]
            if level == 0:
                [
                    "first_industry_code", "first_industry_name", "second_industry_code",
                    "second_industry_name", "third_industry_code", "third_industry_name",
                ]
    """
    order_book_ids = ensure_order_book_ids(order_book_ids, type="Convertible")
    all_dict = _all_instruments_dict(market)
    stock_code_map = {
        all_dict.get(i).stock_code: all_dict.get(i).order_book_id
        for i in order_book_ids if all_dict.get(i)
    }
    # 调用股票行业接口
    res = shenwan.get_instrument_industry(list(stock_code_map.keys()), source, level, date, market)
    if res is None:
        return

    # 转换order_book_id为可转债id
    res.index = res.index.map(stock_code_map)
    return res


@export_as_api(namespace="convertible")
def get_industry(industry, source='citics', date=None, market="cn"):
    """获取行业可转债列表

    :param industry: 行业名称或代码
    :param source: 分类来源。citics 以及 citics_2019: 中信, gildata: 聚源
    :param date: 查询日期，默认为当前最新日期
    :param market:  (Default value = "cn")
    :return: 所属目标行业的order_book_id list or None
    """
    # 调用股票行业接口
    order_book_ids = shenwan.get_industry(industry, source, date, market)
    if order_book_ids is None:
        return
      
    order_book_ids = set(order_book_ids)

    all_dict = _all_instruments_dict(market)
    oids = [ins.order_book_id for ins in all_dict.values() if ins.stock_code in order_book_ids]
    return sorted(oids)
