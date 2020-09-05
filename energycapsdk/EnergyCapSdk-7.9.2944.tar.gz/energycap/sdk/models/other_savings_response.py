# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OtherSavingsResponse(Model):
    """OtherSavingsResponse.

    :param other_savings_id: Other savings identifier
    :type other_savings_id: int
    :param frequency: Other savings frequency
     Possible values are: one-time, continuous, and recurring
    :type frequency: str
    :param other_savings_category:
    :type other_savings_category: ~energycap.sdk.models.OtherSavingsCategory
    :param description: Description
    :type description: str
    :param start_period: Begin period for the other savings
    :type start_period: int
    :param end_period: End period for the other savings
    :type end_period: int
    :param annnual_cycle_start_month: Month the other savings should begin
     This is only set when the other savings type is recurring
    :type annnual_cycle_start_month: int
    :param annual_cycle_end_month: Month the other savings should end
     This is only set when the other savings type is recurring
    :type annual_cycle_end_month: int
    :param value: Amount saved
    :type value: float
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: Create date
    :type created_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param modified_date: Last modified date
    :type modified_date: datetime
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    """

    _attribute_map = {
        'other_savings_id': {'key': 'otherSavingsId', 'type': 'int'},
        'frequency': {'key': 'frequency', 'type': 'str'},
        'other_savings_category': {'key': 'otherSavingsCategory', 'type': 'OtherSavingsCategory'},
        'description': {'key': 'description', 'type': 'str'},
        'start_period': {'key': 'startPeriod', 'type': 'int'},
        'end_period': {'key': 'endPeriod', 'type': 'int'},
        'annnual_cycle_start_month': {'key': 'annnualCycleStartMonth', 'type': 'int'},
        'annual_cycle_end_month': {'key': 'annualCycleEndMonth', 'type': 'int'},
        'value': {'key': 'value', 'type': 'float'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
    }

    def __init__(self, other_savings_id=None, frequency=None, other_savings_category=None, description=None, start_period=None, end_period=None, annnual_cycle_start_month=None, annual_cycle_end_month=None, value=None, created_by=None, created_date=None, modified_by=None, modified_date=None, cost_unit=None):
        super(OtherSavingsResponse, self).__init__()
        self.other_savings_id = other_savings_id
        self.frequency = frequency
        self.other_savings_category = other_savings_category
        self.description = description
        self.start_period = start_period
        self.end_period = end_period
        self.annnual_cycle_start_month = annnual_cycle_start_month
        self.annual_cycle_end_month = annual_cycle_end_month
        self.value = value
        self.created_by = created_by
        self.created_date = created_date
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.cost_unit = cost_unit
