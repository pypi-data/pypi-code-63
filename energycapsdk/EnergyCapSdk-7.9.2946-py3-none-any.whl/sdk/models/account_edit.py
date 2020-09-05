# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountEdit(Model):
    """AccountEdit.

    :param account_code: The account code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 50 characters</span>
    :type account_code: str
    :param account_info: The account info <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 50 characters</span>
    :type account_info: str
    :param cost_center_id: The identifier for the cost center to which the
     account belongs <span class='property-internal'>Topmost
     (CostCenter)</span> <span class='property-internal'>Required</span>
    :type cost_center_id: int
    :param customer_id: The identifier for the customer the account serves.
     This is normally only set for chargeback accounts <span
     class='property-internal'>Required (defined)</span>
    :type customer_id: int
    :param contact_id: The identifier for the account's contact <span
     class='property-internal'>Required (defined)</span>
    :type contact_id: int
    :param active: Indicates if the account is active or inactive <span
     class='property-internal'>Required (defined)</span>
    :type active: bool
    :param accrual_enabled: Indicates if the account is used with accruals
     <span class='property-internal'>Required (defined)</span>
    :type accrual_enabled: bool
    :param postal_code: The address postal code <span
     class='property-internal'>Required when Country is set to US, or CA</span>
     <span class='property-internal'>Must be between 0 and 10 characters</span>
    :type postal_code: str
    :param city: The address city <span class='property-internal'>Must be
     between 0 and 32 characters</span> <span
     class='property-internal'>Required (defined)</span>
    :type city: str
    :param state: The address state <span class='property-internal'>Must be
     between 0 and 3 characters</span> <span class='property-internal'>Required
     (defined)</span>
    :type state: str
    :param country: The address country <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type country: str
    :param line1: The address first line <span class='property-internal'>Must
     be between 0 and 32 characters</span> <span
     class='property-internal'>Required (defined)</span>
    :type line1: str
    :param line2: The address second line <span class='property-internal'>Must
     be between 0 and 32 characters</span> <span
     class='property-internal'>Required (defined)</span>
    :type line2: str
    :param deposit_paid: The date and time the account deposit was paid <span
     class='property-internal'>Required (defined)</span>
    :type deposit_paid: datetime
    :param deposit_return: The date and time the account deposit was returned
     <span class='property-internal'>Required (defined)</span>
    :type deposit_return: datetime
    :param deposit_note: A note related to the account deposit <span
     class='property-internal'>Required (defined)</span>
    :type deposit_note: str
    :param deposit_amount: The account deposit amount <span
     class='property-internal'>Required (defined)</span>
    :type deposit_amount: float
    :param memo: The account memo <span class='property-internal'>Required
     (defined)</span>
    :type memo: str
    :param service_start: The account's service begin date and time <span
     class='property-internal'>Required (defined)</span>
    :type service_start: datetime
    :param service_end: The account's service end date and time <span
     class='property-internal'>Required (defined)</span>
    :type service_end: datetime
    :param general_ledger_id: The identifier for the account's generalLedgerId
     <span class='property-internal'>Required (defined)</span>
    :type general_ledger_id: int
    """

    _validation = {
        'account_code': {'required': True, 'max_length': 50, 'min_length': 0},
        'account_info': {'required': True, 'max_length': 50, 'min_length': 0},
        'cost_center_id': {'required': True},
        'postal_code': {'max_length': 10, 'min_length': 0},
        'city': {'max_length': 32, 'min_length': 0},
        'state': {'max_length': 3, 'min_length': 0},
        'country': {'required': True, 'max_length': 32, 'min_length': 0},
        'line1': {'max_length': 32, 'min_length': 0},
        'line2': {'max_length': 32, 'min_length': 0},
    }

    _attribute_map = {
        'account_code': {'key': 'accountCode', 'type': 'str'},
        'account_info': {'key': 'accountInfo', 'type': 'str'},
        'cost_center_id': {'key': 'costCenterId', 'type': 'int'},
        'customer_id': {'key': 'customerId', 'type': 'int'},
        'contact_id': {'key': 'contactId', 'type': 'int'},
        'active': {'key': 'active', 'type': 'bool'},
        'accrual_enabled': {'key': 'accrualEnabled', 'type': 'bool'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'line1': {'key': 'line1', 'type': 'str'},
        'line2': {'key': 'line2', 'type': 'str'},
        'deposit_paid': {'key': 'depositPaid', 'type': 'iso-8601'},
        'deposit_return': {'key': 'depositReturn', 'type': 'iso-8601'},
        'deposit_note': {'key': 'depositNote', 'type': 'str'},
        'deposit_amount': {'key': 'depositAmount', 'type': 'float'},
        'memo': {'key': 'memo', 'type': 'str'},
        'service_start': {'key': 'serviceStart', 'type': 'iso-8601'},
        'service_end': {'key': 'serviceEnd', 'type': 'iso-8601'},
        'general_ledger_id': {'key': 'generalLedgerId', 'type': 'int'},
    }

    def __init__(self, account_code, account_info, cost_center_id, country, customer_id=None, contact_id=None, active=None, accrual_enabled=None, postal_code=None, city=None, state=None, line1=None, line2=None, deposit_paid=None, deposit_return=None, deposit_note=None, deposit_amount=None, memo=None, service_start=None, service_end=None, general_ledger_id=None):
        super(AccountEdit, self).__init__()
        self.account_code = account_code
        self.account_info = account_info
        self.cost_center_id = cost_center_id
        self.customer_id = customer_id
        self.contact_id = contact_id
        self.active = active
        self.accrual_enabled = accrual_enabled
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country = country
        self.line1 = line1
        self.line2 = line2
        self.deposit_paid = deposit_paid
        self.deposit_return = deposit_return
        self.deposit_note = deposit_note
        self.deposit_amount = deposit_amount
        self.memo = memo
        self.service_start = service_start
        self.service_end = service_end
        self.general_ledger_id = general_ledger_id
