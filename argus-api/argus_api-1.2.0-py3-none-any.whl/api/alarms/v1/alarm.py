"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def add_alarm(
    description: str = None,
    info: str = None,
    references: str = None,
    links: str = None,
    labels: str = None,
    internalReference: str = None,
    signatures: str = None,
    attackCategoryID: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Add new alarm (INTERNAL)
    
    :param str description: Alarm description  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str info: Alarm verbose information  => format:html
    :param list references: Alarm vulnerability references (CVE-numbers, BID-numbers, etc)  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param list links: Links to external descriptions of this alarm  => ((https?|ftp|gopher|telnet|file):((/)|(\\))+[\w\d:\#@%/;$()~_?\\+-=\\\.&]*)
    :param list labels: Tag an alarm with labels  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str internalReference: A link to an internal reference for the alarm  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param list signatures: List of signatures to map to this alarm  => Sanitize by regex [a-zA-Z0-9_/:@~!\+\-\.\?]*
    :param int attackCategoryID: Alarm attack category ID (default 0)
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
    
    url = "{}/alarms/v1/alarm".format(
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
    # Only send description if the argument was provided, dont send null values
    if description is not None:
        body.update({"description": description})
    # Only send attackCategoryID if the argument was provided, dont send null values
    if attackCategoryID is not None:
        body.update({"attackCategoryID": attackCategoryID})
    # Only send info if the argument was provided, dont send null values
    if info is not None:
        body.update({"info": info})
    # Only send references if the argument was provided, dont send null values
    if references is not None:
        body.update({"references": references})
    # Only send links if the argument was provided, dont send null values
    if links is not None:
        body.update({"links": links})
    # Only send labels if the argument was provided, dont send null values
    if labels is not None:
        body.update({"labels": labels})
    # Only send internalReference if the argument was provided, dont send null values
    if internalReference is not None:
        body.update({"internalReference": internalReference})
    # Only send signatures if the argument was provided, dont send null values
    if signatures is not None:
        body.update({"signatures": signatures})

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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def add_alarm_comment(
    id: int,
    comment: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Add alarm comment (INTERNAL)
    
    :param int id: ID of Alarm
    :param str comment: Comment content. Html is allowed, will be sanitized.  => format:html
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/alarms/v1/alarm/{id}/comment".format(
        server_url or settings["api"]["api_url"],
        id=id
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
    # Only send comment if the argument was provided, dont send null values
    if comment is not None:
        body.update({"comment": comment})

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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def delete_alarm(
    id: int,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Delete existing alarm (INTERNAL)
    
    :param int id: ID of Alarm
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import delete
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/alarms/v1/alarm/{id}".format(
        server_url or settings["api"]["api_url"],
        id=id
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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def delete_alarm_comment(
    id: int,
    timestamp: int,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Delete alarm comment (INTERNAL)
    
    :param int id: ID of Alarm
    :param int timestamp: Timestamp of comment
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import delete
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/alarms/v1/alarm/{id}/comment/{timestamp}".format(
        server_url or settings["api"]["api_url"],
        id=id,
        timestamp=timestamp
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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def get_alarm_by_id(
    id: int,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Get alarm by Id (PUBLIC)
    
    :param int id: ID of alarm
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
    
    url = "{}/alarms/v1/alarm/{id}".format(
        server_url or settings["api"]["api_url"],
        id=id
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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def get_alarms(
    keywords: str = None,
    keywordField: str = None,
    keywordMatch: str = "all",
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Get all alarms (PUBLIC)
    
    :param list keywords: Search by keywords
    :param list keywordField: Set field strategy for keyword search
    :param str keywordMatch: Set match strategy for keyword search
    :param int limit: Maximum number of returned alarms
    :param int offset: Skip a number of alarms
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
    
    url = "{}/alarms/v1/alarm".format(
        server_url or settings["api"]["api_url"],
        keywordMatch=keywordMatch,
        limit=limit,
        keywords=keywords,
        keywordField=keywordField,
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
    # Only send keywordMatch if the argument was provided, dont send null values
    if keywordMatch is not None:
        query_parameters.update({"keywordMatch": keywordMatch})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        query_parameters.update({"keywords": keywords})
    # Only send keywordField if the argument was provided, dont send null values
    if keywordField is not None:
        query_parameters.update({"keywordField": keywordField})
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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def map_to_alarm(
    id: int,
    signatures: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Map signatures to alarm (INTERNAL)
    
    :param int id: ID of Alarm
    :param list signatures: Signatures (exist/new) to be mapped to the alarm  => Sanitize by regex [a-zA-Z0-9_/:@~!\+\-\.\?]*
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
    
    url = "{}/alarms/v1/alarm/{id}/map".format(
        server_url or settings["api"]["api_url"],
        id=id
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
    # Only send signatures if the argument was provided, dont send null values
    if signatures is not None:
        body.update({"signatures": signatures})

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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def search_alarms(
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    attackCategoryID: int = None,
    alarmID: int = None,
    alarmReferences: str = None,
    labels: str = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    timeFieldStrategy: str = None,
    timeMatchStrategy: str = None,
    keywords: str = None,
    keywordFieldStrategy: str = None,
    keywordMatchStrategy: str = None,
    signature: str = None,
    sortBy: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    includeMappings: bool = None,
    includeComments: bool = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Get all alarms matching a given search criteria (PUBLIC)
    
    :param int limit: Set this value to set max number of results. By default, no restriction on result set size. 
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default, exclude deleted objects. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). 
    :param list attackCategoryID: A set of IDs for attack categories (alarm category). 
    :param list alarmID: A set of IDs for alarms. 
    :param list alarmReferences: A set of references. It does an exact match. 
    :param list labels: A set of labels. It does an exact match. 
    :param int startTimestamp: Only include alarms based on the set TimeFieldStrategy and TimeMatchStrategy (start timestamp) 
    :param int endTimestamp: Only include alarms based on the set TimeFieldStrategy and TimeMatchStrategy (end timestamp) 
    :param list timeFieldStrategy: TimeFieldStrategy to define which timestamp field(s) to match. (default lastUpdatedTimestamp)
    :param str timeMatchStrategy: TimeMatchStrategy to define how to match startTimestamp and endTimestamp with fields. (default any)
    :param list keywords: A set of keywords matched against alarms based on the set KeywordFieldStrategy and KeywordMatchStrategy. 
    :param list keywordFieldStrategy: KeywordFieldStrategy to define which field(s) to match against keywords. (default all)
    :param str keywordMatchStrategy: KeywordMatchStrategy to define how to match keywords with fields. (default all)
    :param list signature: A set of signatures. It does an exact match. 
    :param list sortBy: List of properties to sort by (prefix with "-" to sort descending). 
    :param list includeFlags: Only include objects which have includeFlags set. 
    :param list excludeFlags: Exclude objects which have excludeFlags set. 
    :param bool includeMappings: Set to include mappings in the search result. (default false)
    :param bool includeComments: Set to include comments in the search result. (default false)
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
    
    url = "{}/alarms/v1/alarm/search".format(
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
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send exclude if the argument was provided, dont send null values
    if exclude is not None:
        body.update({"exclude": exclude})
    # Only send required if the argument was provided, dont send null values
    if required is not None:
        body.update({"required": required})
    # Only send attackCategoryID if the argument was provided, dont send null values
    if attackCategoryID is not None:
        body.update({"attackCategoryID": attackCategoryID})
    # Only send alarmID if the argument was provided, dont send null values
    if alarmID is not None:
        body.update({"alarmID": alarmID})
    # Only send alarmReferences if the argument was provided, dont send null values
    if alarmReferences is not None:
        body.update({"alarmReferences": alarmReferences})
    # Only send labels if the argument was provided, dont send null values
    if labels is not None:
        body.update({"labels": labels})
    # Only send includeMappings if the argument was provided, dont send null values
    if includeMappings is not None:
        body.update({"includeMappings": includeMappings})
    # Only send includeComments if the argument was provided, dont send null values
    if includeComments is not None:
        body.update({"includeComments": includeComments})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send timeFieldStrategy if the argument was provided, dont send null values
    if timeFieldStrategy is not None:
        body.update({"timeFieldStrategy": timeFieldStrategy})
    # Only send timeMatchStrategy if the argument was provided, dont send null values
    if timeMatchStrategy is not None:
        body.update({"timeMatchStrategy": timeMatchStrategy})
    # Only send keywords if the argument was provided, dont send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordFieldStrategy if the argument was provided, dont send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send keywordMatchStrategy if the argument was provided, dont send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        body.update({"signature": signature})
    # Only send sortBy if the argument was provided, dont send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeFlags if the argument was provided, dont send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, dont send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})

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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def unmap(
    id: int,
    signature: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Unmap signatures from alarm (INTERNAL)
    
    :param int id: ID of Alarm
    :param list signature: Signatures to unmap
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
    
    url = "{}/alarms/v1/alarm/{id}/unmap".format(
        server_url or settings["api"]["api_url"],
        id=id,
        signature=signature
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
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        query_parameters.update({"signature": signature})

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
    extending=("alarms", "v1", "alarm"),
    module=argus_cli_module
)
def update_alarm(
    id: int,
    description: str = None,
    info: str = None,
    disabled: bool = None,
    addReferences: str = None,
    deleteReferences: str = None,
    addLinks: str = None,
    deleteLinks: str = None,
    addLabels: str = None,
    deleteLabels: str = None,
    internalReference: str = None,
    attackCategoryID: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Update existing alarm (INTERNAL)
    
    :param int id: ID of Alarm
    :param str description: Update description of alarm  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str info: Update verbose information of alarm  => format:html
    :param bool disabled: Disable or enable alarm (unchanged if not set) 
    :param list addReferences: Add vulnerability references (CVE-numbers, BID-numbers, etc)  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param list deleteReferences: Remove vulnerability references 
    :param list addLinks: Add external links  => ((https?|ftp|gopher|telnet|file):((/)|(\\))+[\w\d:\#@%/;$()~_?\\+-=\\\.&]*)
    :param list deleteLinks: Remove external links 
    :param list addLabels: Add labels  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param list deleteLabels: Remove labels  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str internalReference: A link to an internal reference for the alarm  => [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param int attackCategoryID: Update category of alarm (unchanged if set to 0) (default 0)
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """
    from os import getenv
    from requests import put
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/alarms/v1/alarm/{id}".format(
        server_url or settings["api"]["api_url"],
        id=id
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
    # Only send description if the argument was provided, dont send null values
    if description is not None:
        body.update({"description": description})
    # Only send attackCategoryID if the argument was provided, dont send null values
    if attackCategoryID is not None:
        body.update({"attackCategoryID": attackCategoryID})
    # Only send info if the argument was provided, dont send null values
    if info is not None:
        body.update({"info": info})
    # Only send disabled if the argument was provided, dont send null values
    if disabled is not None:
        body.update({"disabled": disabled})
    # Only send addReferences if the argument was provided, dont send null values
    if addReferences is not None:
        body.update({"addReferences": addReferences})
    # Only send deleteReferences if the argument was provided, dont send null values
    if deleteReferences is not None:
        body.update({"deleteReferences": deleteReferences})
    # Only send addLinks if the argument was provided, dont send null values
    if addLinks is not None:
        body.update({"addLinks": addLinks})
    # Only send deleteLinks if the argument was provided, dont send null values
    if deleteLinks is not None:
        body.update({"deleteLinks": deleteLinks})
    # Only send addLabels if the argument was provided, dont send null values
    if addLabels is not None:
        body.update({"addLabels": addLabels})
    # Only send deleteLabels if the argument was provided, dont send null values
    if deleteLabels is not None:
        body.update({"deleteLabels": deleteLabels})
    # Only send internalReference if the argument was provided, dont send null values
    if internalReference is not None:
        body.update({"internalReference": internalReference})

    query_parameters = {}

    log.debug("PUT %s (headers: %s, body: %s)" % (url, str(headers), str(body) or ""))

    response = put(
        url,
        params=query_parameters or None,
        json=body,
        verify=getenv('REQUESTS_CA_BUNDLE', verify),
        headers=headers
    )

    validate_http_response(response)
    return response.json()

