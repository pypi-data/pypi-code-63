"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("events", "v1", "payload"),
    module=argus_cli_module
)
def get_payload(
    type: str,
    timestamp: int,
    customerID: int,
    eventID: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Fetch specified event payload (PUBLIC)
    
    :param str type: 
    :param int timestamp: 
    :param int customerID: 
    :param str eventID: 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/events/v1/{type}/{timestamp}/{customerID}/{eventID}/payload".format(
        server_url or settings["api"]["api_url"],
        type=type,
        timestamp=timestamp,
        customerID=customerID,
        eventID=eventID
    )
    headers = {
        'User-Agent': 'ArgusToolbelt/',
        'content': 'application/json'
    }

    if not apiKey and "api_key" in settings["api"]:
        apiKey = settings["api"]["api_key"]

    if apiKey:
        headers["Argus-API-Key"] = apiKey
    elif authentication and isinstance(authentication, dict):
        headers.update(authentication)
    elif callable(authentication):
        headers.update(authentication(url))

    body = {}

    query_parameters = {}

    log.debug("GET %s (headers: %s, body: %s)" % (url, str(headers), str(body) or ""))

    response = get(
        url,
        params=query_parameters or None,
        verify=getenv('REQUESTS_CA_BUNDLE', verify),
        headers=headers
    )

    validate_http_response(response)
    return response.json()

