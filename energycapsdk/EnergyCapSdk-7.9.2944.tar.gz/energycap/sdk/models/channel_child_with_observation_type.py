# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChannelChildWithObservationType(Model):
    """ChannelChildWithObservationType.

    :param type:
    :type type: ~energycap.sdk.models.ObservationTypeChild
    :param rule:
    :type rule: ~energycap.sdk.models.ObservationRule
    :param channel_code: The channel code
     Combines
     observationTypeCode:unitCode:observationMethodCode:observationRuleCode:interval
     in minutes
    :type channel_code: str
    :param channel_id: The channel identifier
    :type channel_id: int
    :param interval: The channel interval in seconds.
     Monthly = 2592000
     Weekly = 604800
     Daily = 86400
     Hourly = 3600
     Thirty_Minutes = 1800
     Fifteen_Minutes = 900
    :type interval: int
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'ObservationTypeChild'},
        'rule': {'key': 'rule', 'type': 'ObservationRule'},
        'channel_code': {'key': 'channelCode', 'type': 'str'},
        'channel_id': {'key': 'channelId', 'type': 'int'},
        'interval': {'key': 'interval', 'type': 'int'},
    }

    def __init__(self, type=None, rule=None, channel_code=None, channel_id=None, interval=None):
        super(ChannelChildWithObservationType, self).__init__()
        self.type = type
        self.rule = rule
        self.channel_code = channel_code
        self.channel_id = channel_id
        self.interval = interval
