# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApiKeyResponse(Model):
    """ApiKeyResponse.

    :param api_key_id: The identifier of the API key
    :type api_key_id: int
    :param api_key_name: The name of the API key
    :type api_key_name: str
    :param api_key_description: A description of the API key
    :type api_key_description: str
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: The API key creation date
    :type created_date: datetime
    """

    _attribute_map = {
        'api_key_id': {'key': 'apiKeyId', 'type': 'int'},
        'api_key_name': {'key': 'apiKeyName', 'type': 'str'},
        'api_key_description': {'key': 'apiKeyDescription', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
    }

    def __init__(self, api_key_id=None, api_key_name=None, api_key_description=None, created_by=None, created_date=None):
        super(ApiKeyResponse, self).__init__()
        self.api_key_id = api_key_id
        self.api_key_name = api_key_name
        self.api_key_description = api_key_description
        self.created_by = created_by
        self.created_date = created_date
