"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def attach(
    profileID: int,
    artifactID: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Attach artifact to profile (INTERNAL)
    
    :param int profileID: ID of profile to attach to
    :param list artifactID: Hash ID of artifacts to attach
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
    
    url = "{}/configurationadmin/v1/profile/{profileID}/artifacts/{artifactID}".format(
        server_url or settings["api"]["api_url"],
        profileID=profileID,
        artifactID=artifactID
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def attach_by_name(
    profileName: str,
    groupID: str,
    artifactID: str,
    version: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Attach artifact to profile by profile name and artifact GAV (INTERNAL)
    
    :param str profileName: Name of profile to attach to
    :param str groupID: GroupID of artifact to attach
    :param str artifactID: ArtifactID of artifact to attach
    :param str version: Version of artifact to attach
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
    
    url = "{}/configurationadmin/v1/profile/{profileName}/artifacts/{groupID}/{artifactID}/{version}".format(
        server_url or settings["api"]["api_url"],
        profileName=profileName,
        groupID=groupID,
        artifactID=artifactID,
        version=version
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def attach_detach(
    profileID: int,
    artifactsToAttach: str = None,
    artifactsToDetach: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Attach and detach artifact to given profile (INTERNAL)
    
    :param int profileID: ID of profile to detach from
    :param list artifactsToAttach: 
    :param list artifactsToDetach: 
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
    
    url = "{}/configurationadmin/v1/profile/{profileID}/artifacts".format(
        server_url or settings["api"]["api_url"],
        profileID=profileID
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
    # Only send artifactsToAttach if the argument was provided, dont send null values
    if artifactsToAttach is not None:
        body.update({"artifactsToAttach": artifactsToAttach})
    # Only send artifactsToDetach if the argument was provided, dont send null values
    if artifactsToDetach is not None:
        body.update({"artifactsToDetach": artifactsToDetach})

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


@register_command(
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def create_1(
    name: str = None,
    artifactsToAttach: str = None,
    finalize: bool = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Add new code profile (INTERNAL)
    
    :param str name: [a-zA-Z0-9_\-\.]*
    :param list artifactsToAttach: 
    :param bool finalize: 
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
    
    url = "{}/configurationadmin/v1/profile".format(
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
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send artifactsToAttach if the argument was provided, dont send null values
    if artifactsToAttach is not None:
        body.update({"artifactsToAttach": artifactsToAttach})
    # Only send finalize if the argument was provided, dont send null values
    if finalize is not None:
        body.update({"finalize": finalize})

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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def delete(
    id: int,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Mark code profile as deleted (INTERNAL)
    
    :param int id: ID of profile to delete
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
    
    url = "{}/configurationadmin/v1/profile/{id}".format(
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def detach(
    profileID: int,
    artifactID: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Detach artifact to profile (INTERNAL)
    
    :param int profileID: ID of profile to detach from
    :param str artifactID: Hash ID of artifact to detach
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
    
    url = "{}/configurationadmin/v1/profile/{profileID}/artifacts/{artifactID}".format(
        server_url or settings["api"]["api_url"],
        profileID=profileID,
        artifactID=artifactID
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def detach_by_artifact_by_g_a(
    profileName: str,
    groupID: str,
    artifactID: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Detach artifact from profile by profile name and artifact GAV (INTERNAL)
    
    :param str profileName: Name of profile to detach from
    :param str groupID: GroupID of artifact to detach
    :param str artifactID: ArtifactID of artifact to detach
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
    
    url = "{}/configurationadmin/v1/profile/{profileName}/artifacts/{groupID}/{artifactID}".format(
        server_url or settings["api"]["api_url"],
        profileName=profileName,
        groupID=groupID,
        artifactID=artifactID
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def detach_by_name(
    profileName: str,
    groupID: str,
    artifactID: str,
    version: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Detach artifact from profile by profile name and artifact GAV (INTERNAL)
    
    :param str profileName: Name of profile to detach from
    :param str groupID: GroupID of artifact to detach
    :param str artifactID: ArtifactID of artifact to detach
    :param str version: Version of artifact to detach
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
    
    url = "{}/configurationadmin/v1/profile/{profileName}/artifacts/{groupID}/{artifactID}/{version}".format(
        server_url or settings["api"]["api_url"],
        profileName=profileName,
        groupID=groupID,
        artifactID=artifactID,
        version=version
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def duplicate(
    id: int,
    name: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Duplicate existing code profile (INTERNAL)
    
    :param int id: ID of profile to duplicate
    :param str name: Name of new profile
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
    
    url = "{}/configurationadmin/v1/profile/{id}/duplicate/{name}".format(
        server_url or settings["api"]["api_url"],
        id=id,
        name=name
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def get_by_id_1(
    id: int,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Get code profile by ID (INTERNAL)
    
    :param int id: ID of profile to fetch
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
    
    url = "{}/configurationadmin/v1/profile/{id}".format(
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def get_by_name(
    name: str,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Get code profile by name (INTERNAL)
    
    :param str name: Name of profile to fetch
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
    
    url = "{}/configurationadmin/v1/profile/{name}".format(
        server_url or settings["api"]["api_url"],
        name=name
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def list_1(
    orderDesc: bool = None,
    limit: int = 25,
    orderBy: str = "name",
    offset: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """List code profiles (INTERNAL)
    
    :param bool orderDesc: Sort results descending
    :param int limit: Limit results
    :param str orderBy: Sort results
    :param int offset: Offset results
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
    
    url = "{}/configurationadmin/v1/profile".format(
        server_url or settings["api"]["api_url"],
        limit=limit,
        orderBy=orderBy,
        offset=offset,
        orderDesc=orderDesc
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
    # Only send orderBy if the argument was provided, dont send null values
    if orderBy is not None:
        query_parameters.update({"orderBy": orderBy})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    # Only send orderDesc if the argument was provided, dont send null values
    if orderDesc is not None:
        query_parameters.update({"orderDesc": orderDesc})

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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def search_1(
    searchString: str = None,
    usingArtifact: str = None,
    includeArtifacts: bool = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    includeCreatedTimestamp: bool = None,
    includeLastUpdatedTimestamp: bool = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    includeFlags: int = None,
    excludeFlags: int = None,
    subCriteria: dict = None,
    exclude: bool = None,
    required: bool = None,
    sortBy: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Search code profiles (INTERNAL)
    
    :param str searchString: 
    :param list usingArtifact: 
    :param bool includeArtifacts: 
    :param int startTimestamp: 
    :param int endTimestamp: 
    :param bool includeCreatedTimestamp: 
    :param bool includeLastUpdatedTimestamp: 
    :param int limit: Set this value to set max number of results. By default, no restriction on result set size. 
    :param int offset: Set this value to skip the first (offset) objects. By default, return result from first object. 
    :param bool includeDeleted: Set to true to include deleted objects. By default, exclude deleted objects. 
    :param int includeFlags: Only include objects which have includeFlags set. 
    :param int excludeFlags: Exclude objects which have excludeFlags set. 
    :param list subCriteria: Set additional criterias which are applied using a logical OR. 
    :param bool exclude: Only relevant for subcriteria. If set to true, objects matching this subcriteria object will be excluded. 
    :param bool required: Only relevant for subcriteria. If set to true, objects matching this subcriteria are required (AND-ed together with parent criteria). 
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
    
    url = "{}/configurationadmin/v1/profile/search".format(
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
    # Only send searchString if the argument was provided, dont send null values
    if searchString is not None:
        body.update({"searchString": searchString})
    # Only send usingArtifact if the argument was provided, dont send null values
    if usingArtifact is not None:
        body.update({"usingArtifact": usingArtifact})
    # Only send includeArtifacts if the argument was provided, dont send null values
    if includeArtifacts is not None:
        body.update({"includeArtifacts": includeArtifacts})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send includeCreatedTimestamp if the argument was provided, dont send null values
    if includeCreatedTimestamp is not None:
        body.update({"includeCreatedTimestamp": includeCreatedTimestamp})
    # Only send includeLastUpdatedTimestamp if the argument was provided, dont send null values
    if includeLastUpdatedTimestamp is not None:
        body.update({"includeLastUpdatedTimestamp": includeLastUpdatedTimestamp})
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
    extending=("configurationadmin", "v1", "profile"),
    module=argus_cli_module
)
def update(
    id: int,
    name: str = None,
    finalized: bool = None,
    useForUnknown: bool = None,
    setAsDefault: bool = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> dict:
    """Update code profile (INTERNAL)
    
    :param int id: ID of profile to update
    :param str name: [a-zA-Z0-9_\-\.]*
    :param bool finalized: 
    :param bool useForUnknown: 
    :param bool setAsDefault: 
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
    
    url = "{}/configurationadmin/v1/profile/{id}".format(
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
    # Only send name if the argument was provided, dont send null values
    if name is not None:
        body.update({"name": name})
    # Only send finalized if the argument was provided, dont send null values
    if finalized is not None:
        body.update({"finalized": finalized})
    # Only send useForUnknown if the argument was provided, dont send null values
    if useForUnknown is not None:
        body.update({"useForUnknown": useForUnknown})
    # Only send setAsDefault if the argument was provided, dont send null values
    if setAsDefault is not None:
        body.update({"setAsDefault": setAsDefault})

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

