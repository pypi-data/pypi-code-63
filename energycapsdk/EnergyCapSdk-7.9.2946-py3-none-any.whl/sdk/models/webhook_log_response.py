# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebhookLogResponse(Model):
    """WebhookLogResponse.

    :param webhook_log_id: The identifier of the webhook log
    :type webhook_log_id: long
    :param request_timestamp: The date and time that the webhook was fired
    :type request_timestamp: datetime
    :param result: The HTTP status code that was received from the configured
     url
     0 indicates no response was received from the configured url
    :type result: str
    """

    _attribute_map = {
        'webhook_log_id': {'key': 'webhookLogId', 'type': 'long'},
        'request_timestamp': {'key': 'requestTimestamp', 'type': 'iso-8601'},
        'result': {'key': 'result', 'type': 'str'},
    }

    def __init__(self, webhook_log_id=None, request_timestamp=None, result=None):
        super(WebhookLogResponse, self).__init__()
        self.webhook_log_id = webhook_log_id
        self.request_timestamp = request_timestamp
        self.result = result
