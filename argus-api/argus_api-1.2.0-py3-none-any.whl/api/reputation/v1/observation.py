"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def add_observations(
    sourceID: int = None,
    sourceAlias: str = None,
    observations: dict = None,
    addAddresses: bool = True,
    addDomains: bool = True,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Add reputation observations (INTERNAL)
    
    :param int sourceID: 
    :param str sourceAlias: 
    :param list observations: Observations 
    :param bool addAddresses: Whether add addresses (default true)
    :param bool addDomains: Whether add domains (default true)
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation".format(
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
    # Only send sourceID if the argument was provided, dont send null values
    if sourceID is not None:
        body.update({"sourceID": sourceID})
    # Only send sourceAlias if the argument was provided, dont send null values
    if sourceAlias is not None:
        body.update({"sourceAlias": sourceAlias})
    # Only send addAddresses if the argument was provided, dont send null values
    if addAddresses is not None:
        body.update({"addAddresses": addAddresses})
    # Only send addDomains if the argument was provided, dont send null values
    if addDomains is not None:
        body.update({"addDomains": addDomains})
    # Only send observations if the argument was provided, dont send null values
    if observations is not None:
        body.update({"observations": observations})

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
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def delete_observations(
    sourceAlias: str = None,
    address: str = None,
    fqdn: str = None,
    sourceID: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Delete reputation observations (INTERNAL)
    
    :param str sourceAlias: Source alias
    :param list address: IP Addresses
    :param list fqdn: Domain names
    :param int sourceID: Source ID
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import delete
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation".format(
        server_url or settings["api"]["api_url"],
        sourceID=sourceID,
        sourceAlias=sourceAlias,
        address=address,
        fqdn=fqdn
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
    # Only send sourceID if the argument was provided, dont send null values
    if sourceID is not None:
        query_parameters.update({"sourceID": sourceID})
    # Only send sourceAlias if the argument was provided, dont send null values
    if sourceAlias is not None:
        query_parameters.update({"sourceAlias": sourceAlias})
    # Only send address if the argument was provided, dont send null values
    if address is not None:
        query_parameters.update({"address": address})
    # Only send fqdn if the argument was provided, dont send null values
    if fqdn is not None:
        query_parameters.update({"fqdn": fqdn})

    log.debug("DELETE %s (headers: %s, body: %s)" % (url, str(headers), str(body) or ""))

    response = delete(
        url,
        params=query_parameters or None,
        verify=getenv('REQUESTS_CA_BUNDLE', verify),
        headers=headers
    )

    validate_http_response(response)
    return response.json()


@register_command(
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def fetch_observations_for_domain(
    fqdn: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Look up reputation observations for the given domain (INTERNAL)
    
    :param str fqdn: Domain to fetch observations for
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation/domain/{fqdn}".format(
        server_url or settings["api"]["api_url"],
        fqdn=fqdn
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


@register_command(
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def fetch_observations_for_i_p(
    ip: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Look up reputation observations for the given IP (INTERNAL)
    
    :param str ip: IP address to fetch observations for
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation/ip/{ip}".format(
        server_url or settings["api"]["api_url"],
        ip=ip
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


@register_command(
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def find_address_observations(
    minimumState: int = None,
    minimumConfidence: float = None,
    sourceID: int = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    fromAddress: dict = None,
    afterAddress: dict = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    addresses: dict = None,
    sortBy: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """List IP observations (INTERNAL)
    
    :param int minimumState: 
    :param float minimumConfidence: 
    :param list sourceID: 
    :param int startTimestamp: 
    :param int endTimestamp: 
    :param dict fromAddress: 
    :param dict afterAddress: 
    :param int limit: Set this value to set max number of results. By default, no restriction on result set size. 
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default, exclude deleted objects. 
    :param int includeFlags: Only include objects which have includeFlags set. 
    :param int excludeFlags: Exclude objects which have excludeFlags set. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). 
    :param list addresses: Set of IP addresses 
    :param list sortBy: List of properties to sort by (prefix with "-" to sort descending). 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation/ip/search".format(
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
    # Only send minimumState if the argument was provided, dont send null values
    if minimumState is not None:
        body.update({"minimumState": minimumState})
    # Only send minimumConfidence if the argument was provided, dont send null values
    if minimumConfidence is not None:
        body.update({"minimumConfidence": minimumConfidence})
    # Only send sourceID if the argument was provided, dont send null values
    if sourceID is not None:
        body.update({"sourceID": sourceID})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send fromAddress if the argument was provided, dont send null values
    if fromAddress is not None:
        body.update({"fromAddress": fromAddress})
    # Only send afterAddress if the argument was provided, dont send null values
    if afterAddress is not None:
        body.update({"afterAddress": afterAddress})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send exclude if the argument was provided, dont send null values
    if exclude is not None:
        body.update({"exclude": exclude})
    # Only send required if the argument was provided, dont send null values
    if required is not None:
        body.update({"required": required})
    # Only send addresses if the argument was provided, dont send null values
    if addresses is not None:
        body.update({"addresses": addresses})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})

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
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def find_domain_observations(
    minimumState: int = None,
    minimumConfidence: float = None,
    sourceID: int = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    fromDomainName: dict = None,
    afterDomainName: dict = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    domainNames: dict = None,
    sortBy: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """List domain observations (INTERNAL)
    
    :param int minimumState: 
    :param float minimumConfidence: 
    :param list sourceID: 
    :param int startTimestamp: 
    :param int endTimestamp: 
    :param dict fromDomainName: 
    :param dict afterDomainName: 
    :param int limit: Set this value to set max number of results. By default, no restriction on result set size. 
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default, exclude deleted objects. 
    :param int includeFlags: Only include objects which have includeFlags set. 
    :param int excludeFlags: Exclude objects which have excludeFlags set. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). 
    :param list domainNames: List of Full Qualified Domain Names 
    :param list sortBy: List of properties to sort by (prefix with "-" to sort descending). 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation/domain/search".format(
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
    # Only send minimumState if the argument was provided, dont send null values
    if minimumState is not None:
        body.update({"minimumState": minimumState})
    # Only send minimumConfidence if the argument was provided, dont send null values
    if minimumConfidence is not None:
        body.update({"minimumConfidence": minimumConfidence})
    # Only send sourceID if the argument was provided, dont send null values
    if sourceID is not None:
        body.update({"sourceID": sourceID})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send fromDomainName if the argument was provided, dont send null values
    if fromDomainName is not None:
        body.update({"fromDomainName": fromDomainName})
    # Only send afterDomainName if the argument was provided, dont send null values
    if afterDomainName is not None:
        body.update({"afterDomainName": afterDomainName})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send exclude if the argument was provided, dont send null values
    if exclude is not None:
        body.update({"exclude": exclude})
    # Only send required if the argument was provided, dont send null values
    if required is not None:
        body.update({"required": required})
    # Only send domainNames if the argument was provided, dont send null values
    if domainNames is not None:
        body.update({"domainNames": domainNames})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})

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
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def list_address_observations(
    sourceID: int = None,
    minimumState: int = None,
    minimumConfidence: float = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """List IP observations (INTERNAL)
    
    :param int sourceID: Limit result to observations from specified source
    :param int minimumState: Limit result to observations with this state or higher
    :param float minimumConfidence: Limit result to observations bound to sources with at least this confidence
    :param int limit: Limit result
    :param int offset: Offset result
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation/ip".format(
        server_url or settings["api"]["api_url"],
        limit=limit,
        sourceID=sourceID,
        minimumState=minimumState,
        minimumConfidence=minimumConfidence,
        offset=offset
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
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send sourceID if the argument was provided, dont send null values
    if sourceID is not None:
        query_parameters.update({"sourceID": sourceID})
    # Only send minimumState if the argument was provided, dont send null values
    if minimumState is not None:
        query_parameters.update({"minimumState": minimumState})
    # Only send minimumConfidence if the argument was provided, dont send null values
    if minimumConfidence is not None:
        query_parameters.update({"minimumConfidence": minimumConfidence})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})

    log.debug("GET %s (headers: %s, body: %s)" % (url, str(headers), str(body) or ""))

    response = get(
        url,
        params=query_parameters or None,
        verify=getenv('REQUESTS_CA_BUNDLE', verify),
        headers=headers
    )

    validate_http_response(response)
    return response.json()


@register_command(
    extending=("reputation", "v1", "observation"),
    module=argus_cli_module
)
def list_domain_observations(
    sourceID: int = None,
    minimumState: int = None,
    minimumConfidence: float = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """List domain observations (INTERNAL)
    
    :param int sourceID: Limit result to observations from specified source
    :param int minimumState: Limit result to observations with this state or higher
    :param float minimumConfidence: Limit result to observations bound to sources with at least this confidence
    :param int limit: Limit result
    :param int offset: Offset result
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/reputation/v1/observation/domain".format(
        server_url or settings["api"]["api_url"],
        limit=limit,
        sourceID=sourceID,
        minimumState=minimumState,
        minimumConfidence=minimumConfidence,
        offset=offset
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
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send sourceID if the argument was provided, dont send null values
    if sourceID is not None:
        query_parameters.update({"sourceID": sourceID})
    # Only send minimumState if the argument was provided, dont send null values
    if minimumState is not None:
        query_parameters.update({"minimumState": minimumState})
    # Only send minimumConfidence if the argument was provided, dont send null values
    if minimumConfidence is not None:
        query_parameters.update({"minimumConfidence": minimumConfidence})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})

    log.debug("GET %s (headers: %s, body: %s)" % (url, str(headers), str(body) or ""))

    response = get(
        url,
        params=query_parameters or None,
        verify=getenv('REQUESTS_CA_BUNDLE', verify),
        headers=headers
    )

    validate_http_response(response)
    return response.json()

