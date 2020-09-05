# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountChild(Model):
    """AccountChild.

    :param account_id:
    :type account_id: int
    :param account_code:
    :type account_code: str
    :param account_info:
    :type account_info: str
    :param vendor:
    :type vendor: ~energycap.sdk.models.VendorChild
    :param active:
    :type active: bool
    :param has_calculated_meter:
    :type has_calculated_meter: bool
    :param has_split_parent_meter:
    :type has_split_parent_meter: bool
    :param has_split_child_meter:
    :type has_split_child_meter: bool
    """

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'int'},
        'account_code': {'key': 'accountCode', 'type': 'str'},
        'account_info': {'key': 'accountInfo', 'type': 'str'},
        'vendor': {'key': 'vendor', 'type': 'VendorChild'},
        'active': {'key': 'active', 'type': 'bool'},
        'has_calculated_meter': {'key': 'hasCalculatedMeter', 'type': 'bool'},
        'has_split_parent_meter': {'key': 'hasSplitParentMeter', 'type': 'bool'},
        'has_split_child_meter': {'key': 'hasSplitChildMeter', 'type': 'bool'},
    }

    def __init__(self, account_id=None, account_code=None, account_info=None, vendor=None, active=None, has_calculated_meter=None, has_split_parent_meter=None, has_split_child_meter=None):
        super(AccountChild, self).__init__()
        self.account_id = account_id
        self.account_code = account_code
        self.account_info = account_info
        self.vendor = vendor
        self.active = active
        self.has_calculated_meter = has_calculated_meter
        self.has_split_parent_meter = has_split_parent_meter
        self.has_split_child_meter = has_split_child_meter
