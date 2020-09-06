"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("users", "v2", "group"),
    module=argus_cli_module
)
def get_basic_group(
    shortNameOrID: str,
    domain: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Get a basic group (PUBLIC)
    
    :param str shortNameOrID: Short name or ID of group
    :param str domain: Name or ID of the domain of the group
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/users/v2/group/{shortNameOrID}".format(
        server_url or settings["api"]["api_url"],
        shortNameOrID=shortNameOrID,
        domain=domain
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
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})

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
    extending=("users", "v2", "group"),
    module=argus_cli_module
)
def list_basic_groups(
    domain: str = None,
    subject: str = None,
    customer: str = None,
    excludeFlag: str = None,
    includeFlag: str = None,
    keyword: str = None,
    keywordField: str = None,
    sortBy: str = None,
    limit: int = 25,
    keywordMatch: str = "all",
    offset: int = None,
    includeDeleted: bool = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Returns the basic groups matching the query (PUBLIC)
    
    :param list domain: Domain to search in by short name or id
    :param list subject: Subject to search for by short name or id
    :param list customer: Customer to search for by short name or id
    :param list excludeFlag: Exclude subjects with flag
    :param list includeFlag: Include subjects with flag
    :param list keyword: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param list sortBy: Field to sort by
    :param int limit: Maximum number of returned results
    :param str keywordMatch: Set match strategy for keyword search
    :param int offset: Skip a number of results
    :param bool includeDeleted: Include deleted subjects
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
    
    url = "{}/users/v2/group".format(
        server_url or settings["api"]["api_url"],
        limit=limit,
        keywordMatch=keywordMatch,
        offset=offset,
        domain=domain,
        subject=subject,
        customer=customer,
        includeDeleted=includeDeleted,
        excludeFlag=excludeFlag,
        includeFlag=includeFlag,
        keyword=keyword,
        keywordField=keywordField,
        sortBy=sortBy
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
    # Only send keywordMatch if the argument was provided, dont send null values
    if keywordMatch is not None:
        query_parameters.update({"keywordMatch": keywordMatch})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        query_parameters.update({"domain": domain})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        query_parameters.update({"subject": subject})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        query_parameters.update({"customer": customer})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        query_parameters.update({"includeDeleted": includeDeleted})
    # Only send excludeFlag if the argument was provided, dont send null values
    if excludeFlag is not None:
        query_parameters.update({"excludeFlag": excludeFlag})
    # Only send includeFlag if the argument was provided, dont send null values
    if includeFlag is not None:
        query_parameters.update({"includeFlag": includeFlag})
    # Only send keyword if the argument was provided, dont send null values
    if keyword is not None:
        query_parameters.update({"keyword": keyword})
    # Only send keywordField if the argument was provided, dont send null values
    if keywordField is not None:
        query_parameters.update({"keywordField": keywordField})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        query_parameters.update({"sortBy": sortBy})

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
    extending=("users", "v2", "group"),
    module=argus_cli_module
)
def search_basic_groups(
    domain: str = None,
    subject: str = None,
    ancestor: str = None,
    customer: str = None,
    sortBy: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    permissions: dict = None,
    keywords: str = None,
    keywordMatchStrategy: str = None,
    keywordFieldStrategy: str = None,
    subCriteria: dict = None,
    includeDeleted: bool = None,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Returns the basic groups matching the query (PUBLIC)
    
    :param list domain: Restrict the search to subjects in these domains, by domain ID or name. 
    :param list subject: Restrict search to specific subjects, by ID or shortname 
    :param list ancestor: Restrict search to subjects descending from specific groups, by ID or shortname 
    :param list customer: Restrict search to subjects bound to these customers (by ID or shortname). Customer groups will resolve to all subcustomers as well. 
    :param list sortBy: Define sort order (default name)
    :param list includeFlags: Restrict search to subjects having all of the specified flags. 
    :param list excludeFlags: Exclude subjects with these flags from the search. 
    :param list permissions: Limit search to subjects with one of the given permissions 
    :param list keywords: Keywords to search for 
    :param str keywordMatchStrategy: Search strategy to use when searching (default Match all keywords)
    :param list keywordFieldStrategy: Which fields will be searched for the given keyword (default All supported fields)
    :param list subCriteria: Set additional criteria with AND, OR or AND NOT 
    :param bool includeDeleted: Whether or not to include deleted subjects. (default false)
    :param int limit: The max amount of items to display (default 25)
    :param int offset: The amount of items to skip (default 0)
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
    
    url = "{}/users/v2/group/search".format(
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
    # Only send domain if the argument was provided, dont send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send subject if the argument was provided, dont send null values
    if subject is not None:
        body.update({"subject": subject})
    # Only send ancestor if the argument was provided, dont send null values
    if ancestor is not None:
        body.update({"ancestor": ancestor})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send permissions if the argument was provided, dont send null values
    if permissions is not None:
        body.update({"permissions": permissions})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordMatchStrategy if the argument was provided, dont send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
    # Only send keywordFieldStrategy if the argument was provided, dont send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})

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

