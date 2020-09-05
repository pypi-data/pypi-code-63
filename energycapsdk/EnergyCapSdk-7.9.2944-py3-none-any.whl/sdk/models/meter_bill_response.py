# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterBillResponse(Model):
    """MeterBillResponse.

    :param bill_id: The bill identifier
    :type bill_id: int
    :param batch:
    :type batch: ~energycap.sdk.models.BatchChild
    :param account:
    :type account: ~energycap.sdk.models.AccountChild
    :param begin_date: The bill's begin date
    :type begin_date: datetime
    :param end_date: The bill's end date
    :type end_date: datetime
    :param billing_period: The bill's billing period
    :type billing_period: int
    :param account_period: The bill's accounting period
    :type account_period: int
    :param cost: The meter's bill cost
    :type cost: float
    :param cost_per_day: The meter's bill cost per date
    :type cost_per_day: float
    :param cost_per_unit: The meter's bill cost per unit
    :type cost_per_unit: float
    :param estimated: Indicates if the bill is estimated
    :type estimated: bool
    :param approved: Indicates if the bill has been approved
    :type approved: bool
    :param approve_date: The date and time the bill was approved
    :type approve_date: datetime
    :param approved_by:
    :type approved_by: ~energycap.sdk.models.UserChild
    :param exported: Indicates if the bill has been exported
    :type exported: bool
    :param export_date: The date and time the bill was exported
    :type export_date: datetime
    :param exported_by:
    :type exported_by: ~energycap.sdk.models.UserChild
    :param observation_method:
    :type observation_method: ~energycap.sdk.models.ObservationMethodChild
    :param statement_date: The date and time of the bill statement
    :type statement_date: datetime
    :param due_date: The date and time the bill is due
    :type due_date: datetime
    :param next_reading: The date and time of the next reading
    :type next_reading: datetime
    :param control_code: The bill's control code
    :type control_code: str
    :param invoice_number: The bill's invoice number
    :type invoice_number: str
    :param invoice_pages: The number of pages on the invoice
    :type invoice_pages: int
    :param check_number: The check number
    :type check_number: str
    :param check_date: The date and time of the check
    :type check_date: datetime
    :param pay_status: The pay status of the bill
    :type pay_status: str
    :param cleared_date: The cleared date
    :type cleared_date: datetime
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: The date and time the bill was created
    :type created_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date and time of the most recent modification
    :type modified_date: datetime
    :param void: Indicates if the bill has been voided
    :type void: bool
    :param dirty: Indicates if the bill record has been cleaned. Cleaning is
     an internal EnergyCAP process
    :type dirty: bool
    :param import_verified: Indicates if the import has been verified
    :type import_verified: bool
    :param accrual: Indicates if the bill is an acrrual
    :type accrual: bool
    :param accrual_reversed: Indicates if the bill is a reversed accrual
    :type accrual_reversed: bool
    :param accrual_reversed_date: The date and time the accrual was reversed
    :type accrual_reversed_date: datetime
    :param export_hold: Indicates if the bill is held for export
    :type export_hold: bool
    :param gl_exported: Indicates if the bill has been gl exported
    :type gl_exported: bool
    :param gl_exported_by:
    :type gl_exported_by: ~energycap.sdk.models.UserChild
    :param gl_export_date: The date and time the bill was exported to gl
    :type gl_export_date: datetime
    :param from_vendor: Indicates if the bill is from a vendor
    :type from_vendor: bool
    :param has_been_split: Indicates if the bill has been split
    :type has_been_split: bool
    :param was_split_date: The date and time the bill was split
    :type was_split_date: datetime
    :param trans_ref_num: The transaction reference number of the bill
    :type trans_ref_num: str
    :param payment_type: The payment type of the bill
    :type payment_type: str
    :param actual_amount_paid: The actual amount paid
    :type actual_amount_paid: float
    :param assigned_to:
    :type assigned_to: ~energycap.sdk.models.UserChild
    :param assigned_date: The date and time the bill was assigned to a user
    :type assigned_date: datetime
    :param pay_source: The bill's pay source
    :type pay_source: str
    :param pay_to: Indicates whom the bill paid
    :type pay_to: str
    :param previous_balance: The balance of the previous bill
    :type previous_balance: float
    :param balance_forward: The amount of balance that was forwarded
    :type balance_forward: float
    :param current_charges: The current charges
    :type current_charges: float
    :param usage: The meter's usage
    :type usage: float
    :param use_per_day: The meter's usage per day
    :type use_per_day: float
    :param use_unit:
    :type use_unit: ~energycap.sdk.models.UnitChild
    :param actual_demand: The meter's actual demand
    :type actual_demand: float
    :param actual_demand_unit:
    :type actual_demand_unit: ~energycap.sdk.models.UnitChild
    :param billed_demand: The meter's billed demand
    :type billed_demand: float
    :param billed_demand_unit:
    :type billed_demand_unit: ~energycap.sdk.models.UnitChild
    """

    _attribute_map = {
        'bill_id': {'key': 'billId', 'type': 'int'},
        'batch': {'key': 'batch', 'type': 'BatchChild'},
        'account': {'key': 'account', 'type': 'AccountChild'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'account_period': {'key': 'accountPeriod', 'type': 'int'},
        'cost': {'key': 'cost', 'type': 'float'},
        'cost_per_day': {'key': 'costPerDay', 'type': 'float'},
        'cost_per_unit': {'key': 'costPerUnit', 'type': 'float'},
        'estimated': {'key': 'estimated', 'type': 'bool'},
        'approved': {'key': 'approved', 'type': 'bool'},
        'approve_date': {'key': 'approveDate', 'type': 'iso-8601'},
        'approved_by': {'key': 'approvedBy', 'type': 'UserChild'},
        'exported': {'key': 'exported', 'type': 'bool'},
        'export_date': {'key': 'exportDate', 'type': 'iso-8601'},
        'exported_by': {'key': 'exportedBy', 'type': 'UserChild'},
        'observation_method': {'key': 'observationMethod', 'type': 'ObservationMethodChild'},
        'statement_date': {'key': 'statementDate', 'type': 'iso-8601'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'next_reading': {'key': 'nextReading', 'type': 'iso-8601'},
        'control_code': {'key': 'controlCode', 'type': 'str'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'str'},
        'invoice_pages': {'key': 'invoicePages', 'type': 'int'},
        'check_number': {'key': 'checkNumber', 'type': 'str'},
        'check_date': {'key': 'checkDate', 'type': 'iso-8601'},
        'pay_status': {'key': 'payStatus', 'type': 'str'},
        'cleared_date': {'key': 'clearedDate', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'void': {'key': 'void', 'type': 'bool'},
        'dirty': {'key': 'dirty', 'type': 'bool'},
        'import_verified': {'key': 'importVerified', 'type': 'bool'},
        'accrual': {'key': 'accrual', 'type': 'bool'},
        'accrual_reversed': {'key': 'accrualReversed', 'type': 'bool'},
        'accrual_reversed_date': {'key': 'accrualReversedDate', 'type': 'iso-8601'},
        'export_hold': {'key': 'exportHold', 'type': 'bool'},
        'gl_exported': {'key': 'glExported', 'type': 'bool'},
        'gl_exported_by': {'key': 'glExportedBy', 'type': 'UserChild'},
        'gl_export_date': {'key': 'glExportDate', 'type': 'iso-8601'},
        'from_vendor': {'key': 'fromVendor', 'type': 'bool'},
        'has_been_split': {'key': 'hasBeenSplit', 'type': 'bool'},
        'was_split_date': {'key': 'wasSplitDate', 'type': 'iso-8601'},
        'trans_ref_num': {'key': 'transRefNum', 'type': 'str'},
        'payment_type': {'key': 'paymentType', 'type': 'str'},
        'actual_amount_paid': {'key': 'actualAmountPaid', 'type': 'float'},
        'assigned_to': {'key': 'assignedTo', 'type': 'UserChild'},
        'assigned_date': {'key': 'assignedDate', 'type': 'iso-8601'},
        'pay_source': {'key': 'paySource', 'type': 'str'},
        'pay_to': {'key': 'payTo', 'type': 'str'},
        'previous_balance': {'key': 'previousBalance', 'type': 'float'},
        'balance_forward': {'key': 'balanceForward', 'type': 'float'},
        'current_charges': {'key': 'currentCharges', 'type': 'float'},
        'usage': {'key': 'usage', 'type': 'float'},
        'use_per_day': {'key': 'usePerDay', 'type': 'float'},
        'use_unit': {'key': 'useUnit', 'type': 'UnitChild'},
        'actual_demand': {'key': 'actualDemand', 'type': 'float'},
        'actual_demand_unit': {'key': 'actualDemandUnit', 'type': 'UnitChild'},
        'billed_demand': {'key': 'billedDemand', 'type': 'float'},
        'billed_demand_unit': {'key': 'billedDemandUnit', 'type': 'UnitChild'},
    }

    def __init__(self, bill_id=None, batch=None, account=None, begin_date=None, end_date=None, billing_period=None, account_period=None, cost=None, cost_per_day=None, cost_per_unit=None, estimated=None, approved=None, approve_date=None, approved_by=None, exported=None, export_date=None, exported_by=None, observation_method=None, statement_date=None, due_date=None, next_reading=None, control_code=None, invoice_number=None, invoice_pages=None, check_number=None, check_date=None, pay_status=None, cleared_date=None, created_by=None, created_date=None, modified_by=None, modified_date=None, void=None, dirty=None, import_verified=None, accrual=None, accrual_reversed=None, accrual_reversed_date=None, export_hold=None, gl_exported=None, gl_exported_by=None, gl_export_date=None, from_vendor=None, has_been_split=None, was_split_date=None, trans_ref_num=None, payment_type=None, actual_amount_paid=None, assigned_to=None, assigned_date=None, pay_source=None, pay_to=None, previous_balance=None, balance_forward=None, current_charges=None, usage=None, use_per_day=None, use_unit=None, actual_demand=None, actual_demand_unit=None, billed_demand=None, billed_demand_unit=None):
        super(MeterBillResponse, self).__init__()
        self.bill_id = bill_id
        self.batch = batch
        self.account = account
        self.begin_date = begin_date
        self.end_date = end_date
        self.billing_period = billing_period
        self.account_period = account_period
        self.cost = cost
        self.cost_per_day = cost_per_day
        self.cost_per_unit = cost_per_unit
        self.estimated = estimated
        self.approved = approved
        self.approve_date = approve_date
        self.approved_by = approved_by
        self.exported = exported
        self.export_date = export_date
        self.exported_by = exported_by
        self.observation_method = observation_method
        self.statement_date = statement_date
        self.due_date = due_date
        self.next_reading = next_reading
        self.control_code = control_code
        self.invoice_number = invoice_number
        self.invoice_pages = invoice_pages
        self.check_number = check_number
        self.check_date = check_date
        self.pay_status = pay_status
        self.cleared_date = cleared_date
        self.created_by = created_by
        self.created_date = created_date
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.void = void
        self.dirty = dirty
        self.import_verified = import_verified
        self.accrual = accrual
        self.accrual_reversed = accrual_reversed
        self.accrual_reversed_date = accrual_reversed_date
        self.export_hold = export_hold
        self.gl_exported = gl_exported
        self.gl_exported_by = gl_exported_by
        self.gl_export_date = gl_export_date
        self.from_vendor = from_vendor
        self.has_been_split = has_been_split
        self.was_split_date = was_split_date
        self.trans_ref_num = trans_ref_num
        self.payment_type = payment_type
        self.actual_amount_paid = actual_amount_paid
        self.assigned_to = assigned_to
        self.assigned_date = assigned_date
        self.pay_source = pay_source
        self.pay_to = pay_to
        self.previous_balance = previous_balance
        self.balance_forward = balance_forward
        self.current_charges = current_charges
        self.usage = usage
        self.use_per_day = use_per_day
        self.use_unit = use_unit
        self.actual_demand = actual_demand
        self.actual_demand_unit = actual_demand_unit
        self.billed_demand = billed_demand
        self.billed_demand_unit = billed_demand_unit
