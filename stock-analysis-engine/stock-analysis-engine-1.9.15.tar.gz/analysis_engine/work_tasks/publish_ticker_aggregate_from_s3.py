"""
**Publish Aggregate Ticker Data from S3 Task**

Publish S3 key with aggregated stock data to redis
and s3 (if either of them are running and enabled)

- redis - using `redis-py <https://github.com/andymccurdy/redis-py>`__
- s3 - using boto3

**Sample work_dict request for this method**

`analysis_engine.api_requests.build_publish_ticker_aggregate_from_s3
_request <https://
github.com/AlgoTraders/stock-analysis-engine/blob/master/
analysis_engine/api_requests.py#L426>`__

::

    work_request = {
        'ticker': ticker,
        'ticker_id': ticker_id,
        's3_bucket': s3_bucket_name,
        's3_compiled_bucket': s3_compiled_bucket_name,
        's3_key': s3_key,
        'redis_key': redis_key,
        's3_enabled': s3_enabled,
        'redis_enabled': redis_enabled
    }

.. tip:: This task uses the `analysis_engine.work_tasks.
    custom_task.CustomTask class <https://github.com/A
    lgoTraders/stock-analysis-engine/blob/master/anal
    ysis_engine/work_tasks/custom_task.py>`__ for
    task event handling.

**Supported Environment Variables**

::

    export DEBUG_RESULTS=1

"""

import boto3
import json
import re
import redis
import zlib
import celery.task as celery_task
import analysis_engine.consts as ae_consts
import analysis_engine.build_result as build_result
import analysis_engine.get_task_results as get_task_results
import analysis_engine.work_tasks.custom_task as custom_task
import analysis_engine.set_data_in_redis_key as redis_set
import spylunking.log.setup_logging as log_utils
import analysis_engine.s3_read_contents_from_key as s3_read_contents_from_key

log = log_utils.build_colorized_logger(name=__name__)


@celery_task(
    bind=True,
    base=custom_task.CustomTask,
    queue='publish_ticker_aggregate_from_s3')
def publish_ticker_aggregate_from_s3(
        self,
        work_dict):
    """publish_ticker_aggregate_from_s3

    Publish Aggregated Ticker Data from S3 to Redis

    :param work_dict: dictionary for key/values
    """

    label = 'pub-tic-agg-s3-to-redis'

    log.info(f'task - {label} - start work_dict={work_dict}')

    ticker = ae_consts.TICKER
    ticker_id = ae_consts.TICKER_ID
    rec = {
        'ticker': None,
        'ticker_id': None,
        's3_read_enabled': True,
        's3_upload_enabled': True,
        'redis_enabled': True,
        's3_bucket': None,
        's3_compiled_bucket': None,
        's3_key': None,
        'redis_key': None,
        'updated': None
    }
    res = build_result.build_result(
        status=ae_consts.NOT_RUN,
        err=None,
        rec=rec)

    try:
        ticker = work_dict.get(
            'ticker',
            ae_consts.TICKER)
        ticker_id = int(work_dict.get(
            'ticker_id',
            ae_consts.TICKER_ID))

        if not ticker:
            res = build_result.build_result(
                status=ae_consts.ERR,
                err='missing ticker',
                rec=rec)
            return res

        label = work_dict.get(
            'label',
            label)
        s3_key = work_dict.get(
            's3_key',
            None)
        s3_bucket_name = work_dict.get(
            's3_bucket',
            'pricing')
        s3_compiled_bucket_name = work_dict.get(
            's3_compiled_bucket',
            'compileddatasets')
        redis_key = work_dict.get(
            'redis_key',
            None)
        updated = work_dict.get(
            'updated',
            None)
        enable_s3_upload = work_dict.get(
            's3_upload_enabled',
            ae_consts.ENABLED_S3_UPLOAD)
        enable_redis_publish = work_dict.get(
            'redis_enabled',
            ae_consts.ENABLED_REDIS_PUBLISH)
        serializer = work_dict.get(
            'serializer',
            'json')
        encoding = work_dict.get(
            'encoding',
            'utf-8')

        enable_s3_read = True

        rec['ticker'] = ticker
        rec['ticker_id'] = ticker_id
        rec['s3_bucket'] = s3_bucket_name
        rec['s3_compiled_bucket'] = s3_compiled_bucket_name
        rec['s3_key'] = s3_key
        rec['redis_key'] = redis_key
        rec['updated'] = updated
        rec['s3_read_enabled'] = enable_s3_read
        rec['s3_upload_enabled'] = enable_s3_upload
        rec['redis_enabled'] = enable_redis_publish

        if enable_s3_read:
            log.info(f'{label} parsing s3 values')
            access_key = work_dict.get(
                's3_access_key',
                ae_consts.S3_ACCESS_KEY)
            secret_key = work_dict.get(
                's3_secret_key',
                ae_consts.S3_SECRET_KEY)
            region_name = work_dict.get(
                's3_region_name',
                ae_consts.S3_REGION_NAME)
            service_address = work_dict.get(
                's3_address',
                ae_consts.S3_ADDRESS)
            secure = work_dict.get(
                's3_secure',
                ae_consts.S3_SECURE) == '1'

            endpoint_url = f'http{"s" if secure else ""}://{service_address}'

            log.info(
                f'{label} building s3 endpoint_url={endpoint_url} '
                f'region={region_name}')

            s3 = boto3.resource(
                's3',
                endpoint_url=endpoint_url,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region_name,
                config=boto3.session.Config(
                    signature_version='s3v4')
            )

            try:
                log.info(f'{label} checking bucket={s3_bucket_name} exists')
                if s3.Bucket(s3_bucket_name) not in s3.buckets.all():
                    log.info(f'{label} creating bucket={s3_bucket_name}')
                    s3.create_bucket(
                        Bucket=s3_bucket_name)
            except Exception as e:
                log.info(
                    f'{label} failed creating bucket={s3_bucket_name} '
                    f'with ex={e}')
            # end of try/ex for creating bucket

            try:
                log.info(f'{label} checking bucket={s3_bucket_name} keys')
                date_keys = []
                keys = []
                # {TICKER}_YYYY-DD-MM regex
                reg = r'^.*_\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$'
                for bucket in s3.buckets.all():
                    for key in bucket.objects.all():
                        if (ticker.lower() in key.key.lower() and
                                bool(re.compile(reg).search(key.key))):
                            keys.append(key.key)
                            date_keys.append(
                                key.key.split(f'{ticker}_')[1])
            except Exception as e:
                log.info(
                    f'{label} failed to get bucket={s3_bucket_name} '
                    f'keys with ex={e}')
            # end of try/ex for getting bucket keys

            if keys:
                data = []
                for idx, key in enumerate(keys):
                    try:
                        log.info(
                            f'{label} reading to s3={s3_bucket_name}/{key} '
                            f'updated={updated}')
                        loop_data = s3_read_contents_from_key.\
                            s3_read_contents_from_key(
                                s3=s3,
                                s3_bucket_name=s3_bucket_name,
                                s3_key=key,
                                encoding=encoding,
                                convert_as_json=True)

                        initial_size_value = \
                            len(str(loop_data)) / 1024000
                        initial_size_str = ae_consts.to_f(initial_size_value)
                        if ae_consts.ev('DEBUG_S3', '0') == '1':
                            log.info(
                                f'{label} read s3={s3_bucket_name}/{key} '
                                f'data={ae_consts.ppj(loop_data)}')
                        else:
                            log.info(
                                f'{label} read s3={s3_bucket_name}/{key} data '
                                f'size={initial_size_str} MB')
                        data.append({f'{date_keys[idx]}': loop_data})
                    except Exception as e:
                        err = (
                            f'{label} failed reading bucket={s3_bucket_name} '
                            f'key={key} ex={e}')
                        log.error(
                            err)
                        res = build_result.build_result(
                            status=ae_consts.NOT_RUN,
                            err=err,
                            rec=rec)
                    # end of try/ex for creating bucket
            else:
                log.info(
                    f'{label} No keys found in S3 '
                    f'bucket={s3_bucket_name} for ticker={ticker}')
        else:
            log.info(
                f'{label} SKIP S3 read bucket={s3_bucket_name} '
                f'ticker={ticker}')
        # end of if enable_s3_read

        if data and enable_s3_upload:
            try:
                log.info(
                    f'{label} checking bucket={s3_compiled_bucket_name} '
                    'exists')
                if s3.Bucket(s3_compiled_bucket_name) not in s3.buckets.all():
                    log.info(
                        f'{label} creating bucket={s3_compiled_bucket_name}')
                    s3.create_bucket(
                        Bucket=s3_compiled_bucket_name)
            except Exception as e:
                log.info(
                    f'{label} failed creating '
                    f'bucket={s3_compiled_bucket_name} with ex={e}')
            # end of try/ex for creating bucket

            try:
                cmpr_data = zlib.compress(json.dumps(data).encode(encoding), 9)

                if ae_consts.ev('DEBUG_S3', '0') == '1':
                    log.info(
                        f'{label} uploading to '
                        f's3={s3_compiled_bucket_name}/{s3_key} '
                        f'data={ae_consts.ppj(loop_data)} updated={updated}')
                else:
                    sizes = {'MB': 1024000,
                             'GB': 1024000000,
                             'TB': 1024000000000,
                             'PB': 1024000000000000}
                    initial_size_value = len(str(data))
                    org_data_size = 'MB'
                    for key in sizes.keys():
                        size = float(initial_size_value) / float(sizes[key])
                        if size > 1024:
                            continue
                        org_data_size = key
                        initial_size_value = size
                        break
                    initial_size_str = ae_consts.to_f(initial_size_value)

                    cmpr_data_size_value = len(cmpr_data)
                    cmpr_data_size = 'MB'
                    for key in sizes.keys():
                        size = float(cmpr_data_size_value) / float(sizes[key])
                        if size > 1024:
                            continue
                        cmpr_data_size = key
                        cmpr_data_size_value = size
                        break
                    cmpr_size_str = ae_consts.to_f(cmpr_data_size_value)
                    log.info(
                        f'{label} uploading to '
                        f's3={s3_compiled_bucket_name}/{s3_key} data '
                        f'original_size={initial_size_str} {org_data_size} '
                        f'compressed_size={cmpr_size_str} {cmpr_data_size} '
                        f'updated={updated}')
                s3.Bucket(s3_compiled_bucket_name).put_object(
                    Key=s3_key,
                    Body=cmpr_data)
            except Exception as e:
                log.error(
                    f'{label} failed '
                    f'uploading bucket={s3_compiled_bucket_name} '
                    f'key={s3_key} ex={e}')
            # end of try/ex for creating bucket
        else:
            log.info(
                f'{label} SKIP S3 upload bucket={s3_bucket_name} key={s3_key}')
        # end of if enable_s3_upload

        if data and enable_redis_publish:
            redis_address = work_dict.get(
                'redis_address',
                ae_consts.REDIS_ADDRESS)
            redis_key = work_dict.get(
                'redis_key',
                ae_consts.REDIS_KEY)
            redis_password = work_dict.get(
                'redis_password',
                ae_consts.REDIS_PASSWORD)
            redis_db = work_dict.get(
                'redis_db',
                None)
            if not redis_db:
                redis_db = ae_consts.REDIS_DB
            redis_expire = None
            if 'redis_expire' in work_dict:
                redis_expire = work_dict.get(
                    'redis_expire',
                    ae_consts.REDIS_EXPIRE)
            log.info(
                f'redis enabled address={redis_address}@{redis_db} '
                f'key={redis_key}')
            redis_host = redis_address.split(':')[0]
            redis_port = redis_address.split(':')[1]
            try:
                if ae_consts.ev('DEBUG_REDIS', '0') == '1':
                    log.info(
                        f'{label} publishing redis={redis_host}:{redis_port} '
                        f'db={redis_db} key={redis_key} updated={updated} '
                        f'expire={redis_expire} data={ae_consts.ppj(data)}')
                else:
                    log.info(
                        f'{label} publishing redis={redis_host}:{redis_port} '
                        f'db={redis_db} key={redis_key} '
                        f'updated={updated} expire={redis_expire}')
                # end of if/else

                rc = redis.Redis(
                    host=redis_host,
                    port=redis_port,
                    password=redis_password,
                    db=redis_db)

                redis_set_res = redis_set.set_data_in_redis_key(
                    label=label,
                    client=rc,
                    key=redis_key,
                    data=data,
                    serializer=serializer,
                    encoding=encoding,
                    expire=redis_expire,
                    px=None,
                    nx=False,
                    xx=False)

                log.info(
                    f'{label} redis_set '
                    f'status={ae_consts.get_status(redis_set_res["status"])} '
                    f'err={redis_set_res["err"]}')

            except Exception as e:
                log.error(
                    f'{label} failed - redis publish to '
                    f'key={redis_key} ex={e}')
            # end of try/ex for creating bucket
        else:
            log.info(f'{label} SKIP REDIS publish key={redis_key}')
        # end of if enable_redis_publish

        res = build_result.build_result(
            status=ae_consts.SUCCESS,
            err=None,
            rec=rec)

    except Exception as e:
        res = build_result.build_result(
            status=ae_consts.ERR,
            err=(f'failed - publish_from_s3 dict={work_dict} with ex={e}'),
            rec=rec)
        log.error(f'{label} - {res["err"]}')
    # end of try/ex

    log.info(
        'task - publish_from_s3 done - '
        f'{label} - status={ae_consts.get_status(res["status"])}')

    return get_task_results.get_task_results(
        work_dict=work_dict,
        result=res)
# end of publish_ticker_aggregate_from_s3


def run_publish_ticker_aggregate_from_s3(
        work_dict):
    """run_publish_ticker_aggregate_from_s3

    Celery wrapper for running without celery

    :param work_dict: task data
    """

    label = work_dict.get(
        'label',
        '')

    log.info(f'run_publish_ticker_aggregate_from_s3 - {label} - start')

    response = build_result.build_result(
        status=ae_consts.NOT_RUN,
        err=None,
        rec={})
    task_res = {}

    # allow running without celery
    if ae_consts.is_celery_disabled(
            work_dict=work_dict):
        work_dict['celery_disabled'] = True
        task_res = publish_ticker_aggregate_from_s3(
            work_dict=work_dict)
        if task_res:
            response = task_res.get(
                'result',
                task_res)
            if ae_consts.ev('DEBUG_RESULTS', '0') == '1':
                response_details = response
                try:
                    response_details = ae_consts.ppj(response)
                except Exception:
                    response_details = response
                log.info(f'{label} task result={response_details}')
        else:
            log.error(
                f'{label} celery was disabled but the task={response} '
                'did not return anything')
        # end of if response
    else:
        task_res = publish_ticker_aggregate_from_s3.delay(
            work_dict=work_dict)
        rec = {
            'task_id': task_res
        }
        response = build_result.build_result(
            status=ae_consts.SUCCESS,
            err=None,
            rec=rec)
    # if celery enabled

    if response:
        if ae_consts.ev('DEBUG_RESULTS', '0') == '1':
            log.info(
                f'run_publish_ticker_aggregate_from_s3 - {label} - done '
                f'status={ae_consts.get_status(response["status"])} '
                f'err={response["err"]} rec={response["rec"]}')
        else:
            log.info(
                f'run_publish_ticker_aggregate_from_s3 - {label} - done '
                f'status={ae_consts.get_status(response["status"])} '
                f'err={response["err"]}')
    else:
        log.info(
            f'run_publish_ticker_aggregate_from_s3 - {label} - done '
            'no response')
    # end of if/else response

    return response
# end of run_publish_ticker_aggregate_from_s3
