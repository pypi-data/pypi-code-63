"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("componentadmin", "v1", "properties"),
    module=argus_cli_module
)
def get_properties(
    exact: bool = None,
    identifiers: dict = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Fetch all properties from specified component (INTERNAL)
    
    :param bool exact: 
    :param dict identifiers: 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises RemoteInvocationFailedException: on 409
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/componentadmin/v1/properties".format(
        server_url or settings["api"]["api_url"],
        
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
    # Only send exact if the argument was provided, dont send null values
    if exact is not None:
        body.update({"exact": exact})
    # Only send identifiers if the argument was provided, dont send null values
    if identifiers is not None:
        body.update({"identifiers": identifiers})

    query_parameters = {}

    log.debug("POST %s (headers: %s, body: %s)" % (url, str(headers), str(body) or ""))

    response = post(
        url,
        params=query_parameters or None,
        json=body,
        verify=getenv('REQUESTS_CA_BUNDLE', verify),
        headers=headers
    )

    validate_http_response(response)
    return response.json()

