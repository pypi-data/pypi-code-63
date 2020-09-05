# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CostCenterDigestActualMonthlyResponse(Model):
    """CostCenterDigestActualMonthlyResponse.

    :param cost_center_code: The costCenter code
    :type cost_center_code: str
    :param cost_center_info: The costCenter info
    :type cost_center_info: str
    :param cost_center_id: The costCenter identifier
    :type cost_center_id: int
    :param updated: The date and time the data was updated
    :type updated: datetime
    :param global_use_unit:
    :type global_use_unit: ~energycap.sdk.models.UnitChild
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param commodities: An array of monthly data per commodity
    :type commodities:
     list[~energycap.sdk.models.CostCenterDigestActualMonthlyResponseCommodityData]
    :param results: An array of monthly data
    :type results:
     list[~energycap.sdk.models.CostCenterDigestActualMonthlyResponseResults]
    """

    _attribute_map = {
        'cost_center_code': {'key': 'costCenterCode', 'type': 'str'},
        'cost_center_info': {'key': 'costCenterInfo', 'type': 'str'},
        'cost_center_id': {'key': 'costCenterId', 'type': 'int'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'global_use_unit': {'key': 'globalUseUnit', 'type': 'UnitChild'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'commodities': {'key': 'commodities', 'type': '[CostCenterDigestActualMonthlyResponseCommodityData]'},
        'results': {'key': 'results', 'type': '[CostCenterDigestActualMonthlyResponseResults]'},
    }

    def __init__(self, cost_center_code=None, cost_center_info=None, cost_center_id=None, updated=None, global_use_unit=None, cost_unit=None, commodities=None, results=None):
        super(CostCenterDigestActualMonthlyResponse, self).__init__()
        self.cost_center_code = cost_center_code
        self.cost_center_info = cost_center_info
        self.cost_center_id = cost_center_id
        self.updated = updated
        self.global_use_unit = global_use_unit
        self.cost_unit = cost_unit
        self.commodities = commodities
        self.results = results
