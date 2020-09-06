"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("authentication", "v1", "password", "authenticate"),
    module=argus_cli_module
)
def authenticate_1(
    userName: str = None,
    domain: str = None,
    password: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Initiate a new user session using Password authentication (PUBLIC)
    
    :param str userName: Username to authenticate 
    :param str domain: User domain 
    :param str password: Static Argus-password for user 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/authentication/v1/password/authenticate".format(
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
    # Only send userName if the argument was provided, dont send null values
    if userName is not None:
        body.update({"userName": userName})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})

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


@register_command(
    extending=("authentication", "v1", "password", "authenticate"),
    module=argus_cli_module
)
def password_user_authorization(
    operation: str = None,
    context: dict = None,
    nextURI: str = None,
    password: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Request an authorization token using password credentials (DEV)
    
    :param str operation: The name of the operation to authorize 
    :param dict context: Context variables to scope this authorization. All context variables required by the executing service must be present and equal to those provided here. 
    :param str nextURI: The URI to redirect/route to after successful authorization. The URI will be validated according to policy. The authorization token returned from successful authorization should be appended as a query parameter to this URI. 
    :param str password: The current users ARGUS password 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/authentication/v1/password/authorize".format(
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
    # Only send operation if the argument was provided, dont send null values
    if operation is not None:
        body.update({"operation": operation})
    # Only send context if the argument was provided, dont send null values
    if context is not None:
        body.update({"context": context})
    # Only send nextURI if the argument was provided, dont send null values
    if nextURI is not None:
        body.update({"nextURI": nextURI})
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})

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

