# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillSplitParentDetailsResponse(Model):
    """BillSplitParentDetailsResponse.

    :param split_parent_account:
    :type split_parent_account: ~energycap.sdk.models.AccountChild
    :param split_parent_meter:
    :type split_parent_meter: ~energycap.sdk.models.MeterChild
    :param begin_period: First billing period that the bill split was active
     for
    :type begin_period: int
    :param end_period: Last billing period that the bill split was active for
    :type end_period: int
    """

    _attribute_map = {
        'split_parent_account': {'key': 'splitParentAccount', 'type': 'AccountChild'},
        'split_parent_meter': {'key': 'splitParentMeter', 'type': 'MeterChild'},
        'begin_period': {'key': 'beginPeriod', 'type': 'int'},
        'end_period': {'key': 'endPeriod', 'type': 'int'},
    }

    def __init__(self, split_parent_account=None, split_parent_meter=None, begin_period=None, end_period=None):
        super(BillSplitParentDetailsResponse, self).__init__()
        self.split_parent_account = split_parent_account
        self.split_parent_meter = split_parent_meter
        self.begin_period = begin_period
        self.end_period = end_period
