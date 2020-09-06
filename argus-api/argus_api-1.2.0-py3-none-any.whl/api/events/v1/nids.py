"""Autogenerated API"""
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from requests import Response

log = logging.getLogger(__name__)


@register_command(
    extending=("events", "v1", "nids"),
    module=argus_cli_module
)
def find_n_i_d_s_events(
    skipFutureEvents: bool = None,
    exclude: bool = None,
    eventIdentifier: dict = None,
    locationID: int = None,
    severity: str = None,
    customer: str = None,
    alarmID: int = None,
    attackCategoryID: int = None,
    sourceGeoCountry: str = None,
    destinationGeoCountry: str = None,
    geoCountry: str = None,
    properties: dict = None,
    exactMatchProperties: bool = None,
    sensorID: int = None,
    subCriteria: dict = None,
    signature: str = None,
    lastUpdatedTimestamp: int = None,
    indexStartTime: int = None,
    indexEndTime: int = None,
    destinationIP: str = None,
    sourceIP: str = None,
    ip: str = None,
    destinationPort: str = None,
    sourcePort: str = None,
    port: str = None,
    minSeverity: str = None,
    maxSeverity: str = None,
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    customerID: int = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    sortBy: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> Response:
    """Search for NIDS events (PUBLIC)
    
    :param bool skipFutureEvents: 
    :param bool exclude: 
    :param list eventIdentifier: 
    :param list locationID: 
    :param list severity: 
    :param list customer: 
    :param list alarmID: 
    :param list attackCategoryID: 
    :param list sourceGeoCountry: 
    :param list destinationGeoCountry: 
    :param list geoCountry: 
    :param dict properties: 
    :param bool exactMatchProperties: 
    :param list sensorID: 
    :param list subCriteria: 
    :param list signature: 
    :param int lastUpdatedTimestamp: 
    :param int indexStartTime: 
    :param int indexEndTime: 
    :param list destinationIP: 
    :param list sourceIP: 
    :param list ip: 
    :param list destinationPort: 
    :param list sourcePort: 
    :param list port: 
    :param str minSeverity: 
    :param str maxSeverity: 
    :param int limit: Limit results 
    :param int offset: Offset results 
    :param bool includeDeleted: Also include deleted objects (where implemented) 
    :param list customerID: DEPRECATED! Use customer instead 
    :param int startTimestamp: Search objects from this timestamp 
    :param int endTimestamp: Search objects until this timestamp 
    :param list sortBy: Order results by these properties (prefix with - to sort descending) 
    :param list includeFlags: Search objects with these flags set 
    :param list excludeFlags: Exclude objects with these flags set 
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object or dictionary translated from JSON
    """
    from os import getenv
    from requests import post
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/events/v1/nids/search".format(
        server_url or settings["api"]["api_url"],
        
    )
    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }
    if json:
        headers['content'] = 'application/json'

    if not apiKey and "api_key" in settings["api"]:
        apiKey = settings["api"]["api_key"]

    if apiKey:
        headers["Argus-API-Key"] = apiKey
    elif authentication and isinstance(authentication, dict):
        headers.update(authentication)
    elif callable(authentication):
        headers.update(authentication(url))

    body = {}
    # Only send skipFutureEvents if the argument was provided, dont send null values
    if skipFutureEvents is not None:
        body.update({"skipFutureEvents": skipFutureEvents})
    # Only send exclude if the argument was provided, dont send null values
    if exclude is not None:
        body.update({"exclude": exclude})
    # Only send eventIdentifier if the argument was provided, dont send null values
    if eventIdentifier is not None:
        body.update({"eventIdentifier": eventIdentifier})
    # Only send locationID if the argument was provided, dont send null values
    if locationID is not None:
        body.update({"locationID": locationID})
    # Only send severity if the argument was provided, dont send null values
    if severity is not None:
        body.update({"severity": severity})
    # Only send customer if the argument was provided, dont send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send alarmID if the argument was provided, dont send null values
    if alarmID is not None:
        body.update({"alarmID": alarmID})
    # Only send attackCategoryID if the argument was provided, dont send null values
    if attackCategoryID is not None:
        body.update({"attackCategoryID": attackCategoryID})
    # Only send sourceGeoCountry if the argument was provided, dont send null values
    if sourceGeoCountry is not None:
        body.update({"sourceGeoCountry": sourceGeoCountry})
    # Only send destinationGeoCountry if the argument was provided, dont send null values
    if destinationGeoCountry is not None:
        body.update({"destinationGeoCountry": destinationGeoCountry})
    # Only send geoCountry if the argument was provided, dont send null values
    if geoCountry is not None:
        body.update({"geoCountry": geoCountry})
    # Only send properties if the argument was provided, dont send null values
    if properties is not None:
        body.update({"properties": properties})
    # Only send exactMatchProperties if the argument was provided, dont send null values
    if exactMatchProperties is not None:
        body.update({"exactMatchProperties": exactMatchProperties})
    # Only send sensorID if the argument was provided, dont send null values
    if sensorID is not None:
        body.update({"sensorID": sensorID})
    # Only send subCriteria if the argument was provided, dont send null values
    if subCriteria is not None:
        body.update({"subCriteria": subCriteria})
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        body.update({"signature": signature})
    # Only send lastUpdatedTimestamp if the argument was provided, dont send null values
    if lastUpdatedTimestamp is not None:
        body.update({"lastUpdatedTimestamp": lastUpdatedTimestamp})
    # Only send indexStartTime if the argument was provided, dont send null values
    if indexStartTime is not None:
        body.update({"indexStartTime": indexStartTime})
    # Only send indexEndTime if the argument was provided, dont send null values
    if indexEndTime is not None:
        body.update({"indexEndTime": indexEndTime})
    # Only send destinationIP if the argument was provided, dont send null values
    if destinationIP is not None:
        body.update({"destinationIP": destinationIP})
    # Only send sourceIP if the argument was provided, dont send null values
    if sourceIP is not None:
        body.update({"sourceIP": sourceIP})
    # Only send ip if the argument was provided, dont send null values
    if ip is not None:
        body.update({"ip": ip})
    # Only send destinationPort if the argument was provided, dont send null values
    if destinationPort is not None:
        body.update({"destinationPort": destinationPort})
    # Only send sourcePort if the argument was provided, dont send null values
    if sourcePort is not None:
        body.update({"sourcePort": sourcePort})
    # Only send port if the argument was provided, dont send null values
    if port is not None:
        body.update({"port": port})
    # Only send minSeverity if the argument was provided, dont send null values
    if minSeverity is not None:
        body.update({"minSeverity": minSeverity})
    # Only send maxSeverity if the argument was provided, dont send null values
    if maxSeverity is not None:
        body.update({"maxSeverity": maxSeverity})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, dont send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
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
    return response.json() if json else response


@register_command(
    extending=("events", "v1", "nids"),
    module=argus_cli_module
)
def list_n_i_d_s_events(
    customerID: int = None,
    signature: str = None,
    ip: str = None,
    startTimestamp: str = "-24hours",
    endTimestamp: str = "now",
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = True,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
  ) -> Response:
    """Simple search for NIDS events (PUBLIC)
    
    :param list customerID: Limit to customerID
    :param list signature: Limit to signature
    :param list ip: Limit to ip/network
    :param str startTimestamp: Limit to events after this timestamp (default is last 24 hours).
    :param str endTimestamp: Limit to events before this timestamp.
    :param int limit: Limit results
    :param int offset: Offset results
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object or dictionary translated from JSON
    """
    from os import getenv
    from requests import get
    from argus_api._validators import validate_http_response
    
    from argus_cli.settings import settings
    
    url = "{}/events/v1/nids".format(
        server_url or settings["api"]["api_url"],
        startTimestamp=startTimestamp,
        endTimestamp=endTimestamp,
        limit=limit,
        customerID=customerID,
        signature=signature,
        ip=ip,
        offset=offset
    )
    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }
    if json:
        headers['content'] = 'application/json'

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
    # Only send startTimestamp if the argument was provided, dont send null values
    if startTimestamp is not None:
        query_parameters.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, dont send null values
    if endTimestamp is not None:
        query_parameters.update({"endTimestamp": endTimestamp})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})
    # Only send signature if the argument was provided, dont send null values
    if signature is not None:
        query_parameters.update({"signature": signature})
    # Only send ip if the argument was provided, dont send null values
    if ip is not None:
        query_parameters.update({"ip": ip})
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
    return response.json() if json else response

