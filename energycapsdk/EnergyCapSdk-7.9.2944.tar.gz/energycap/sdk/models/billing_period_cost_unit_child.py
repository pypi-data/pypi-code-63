# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillingPeriodCostUnitChild(Model):
    """BillingPeriodCostUnitChild.

    :param cost: The total cost.
    :type cost: float
    :param unit:
    :type unit: ~energycap.sdk.models.UnitChild
    """

    _attribute_map = {
        'cost': {'key': 'cost', 'type': 'float'},
        'unit': {'key': 'unit', 'type': 'UnitChild'},
    }

    def __init__(self, cost=None, unit=None):
        super(BillingPeriodCostUnitChild, self).__init__()
        self.cost = cost
        self.unit = unit
