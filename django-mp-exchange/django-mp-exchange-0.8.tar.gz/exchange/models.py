
from functools import partial

from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel

from exchange.utils import format_printable_price, get_price_factory

from exchange.managers import MultiCurrencyManager

from exchange.constants import (
    CURRENCY_UAH,
    CURRENCIES,
    CURRENCY_NAMES
)


class ExchangeRates(SingletonModel):

    usd = models.FloatField(_('USD'), default=1)

    eur = models.FloatField(_('EUR'), default=1)

    usd_eur = models.FloatField(_('USD - EUR'), default=1)

    def __str__(self):
        return 'usd: {}, eur: {}, usd - eur: {}'.format(
            self.usd,
            self.eur,
            self.usd_eur)

    @classmethod
    def update_prices(cls, queryset):

        rates = ExchangeRates.objects.get()

        field = lambda c: 'price_{}'.format(CURRENCY_NAMES[c])

        for src, src_name in CURRENCIES:

            params = {}

            for dst, dst_name in CURRENCIES:
                price_factory = get_price_factory(rates, src, dst)

                params[field(dst)] = price_factory(F('price_retail'))

            queryset.filter(initial_currency=src).update(**params)

    class Meta:
        verbose_name = _('Exchange rates')
        verbose_name_plural = _('Exchange rates')


class MultiCurrencyPrice(models.Model):

    price_retail = models.FloatField(_('Retail price'))

    price_wholesale = models.FloatField(
        _('Wholesale price'),
        default=0)

    price_usd = models.FloatField(default=0)

    price_eur = models.FloatField(default=0)

    price_uah = models.FloatField(default=0)

    initial_currency = models.PositiveIntegerField(
        _('Currency'), choices=CURRENCIES, default=CURRENCY_UAH)

    objects = MultiCurrencyManager()

    @property
    def price(self):
        return getattr(self, 'price_{}'.format(CURRENCY_NAMES[self.currency]))

    @property
    def printable_price(self):
        return format_printable_price(self.price, self.currency)

    @property
    def currency(self):
        return getattr(self, 'annotated_currency', CURRENCY_UAH)

    @property
    def printable_price(self):
        return format_printable_price(self.price, self.currency)

    @property
    def schema_price(self):
        return str(self.price).replace(',', '.')

    @property
    def schema_currency(self):
        return CURRENCY_NAMES[self.currency].upper()

    @classmethod
    def format_printable_price(cls, *args, **kwargs):
        return format_printable_price(*args, **kwargs)

    @property
    def price_values(self):

        fields = [
            'price_wholesale',
            'price_retail',
            'initial_currency',
            'price_usd',
            'price_eur',
            'price_uah'
        ]

        return {field: getattr(self, field) for field in fields}

    class Meta:
        abstract = True
