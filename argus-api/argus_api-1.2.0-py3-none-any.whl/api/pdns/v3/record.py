"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("pdns", "v3", "record"),
    module=argus_cli_module
)
def submit_p_d_n_s_records_bulk(
    records: dict = None,
    ignoreOnFailed: bool = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Submit PassiveDNS records in a bulk operation (DEV)
    
    :param list records: PDNS records for submission. 
    :param bool ignoreOnFailed: Set this value for successful response even failures occur while submitting. (default false)
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/pdns/v3/record".format(
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
    # Only send records if the argument was provided, dont send null values
    if records is not None:
        body.update({"records": records})
    # Only send ignoreOnFailed if the argument was provided, dont send null values
    if ignoreOnFailed is not None:
        body.update({"ignoreOnFailed": ignoreOnFailed})

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

