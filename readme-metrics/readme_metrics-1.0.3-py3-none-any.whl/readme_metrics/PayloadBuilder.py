import json
import sys
import time
import pkg_resources
from typing import List
from urllib import parse

import requests
from readme_metrics import ResponseInfoWrapper
from werkzeug import Request

from readme_metrics.util import util_exclude_keys, util_filter_keys


class PayloadBuilder:
    """
    Internal builder class that handles the construction of the request and response
    portions of the payload sent to the ReadMe API.

    Attributes:
        blacklist (List[str]): Cached blacklist for current PayloadBuilder instance
        whitelist (List[str]): Cached whitelist for current PayloadBuilder instance
        development_mode (bool): Cached development mode parameter for current
            PayloadBuilder instance
        grouping_function ([type]): Cached grouping function for current PayloadBuilder
            instance
    """

    def __init__(
        self,
        blacklist: List[str],
        whitelist: List[str],
        development_mode: bool,
        grouping_function,
    ):
        """Creates a PayloadBuilder instance with the supplied configuration

        Args:
            blacklist (List[str]): Header/JSON body blacklist
            whitelist (List[str]): Header/JSON body whitelist
            development_mode (bool): Development mode flag passed to ReadMe
            grouping_function ([type]): Grouping function to generate an identity
                payload
        """
        self.blacklist = blacklist
        self.whitelist = whitelist
        self.development_mode = "true" if development_mode else "false"
        self.grouping_function = grouping_function

    def __call__(self, request: Request, response: ResponseInfoWrapper) -> dict:
        """Builds a HAR payload encompassing the request & response data

        Args:
            request (Request): Request information to use
            response (ResponseInfoWrapper): Response information to use

        Returns:
            dict: Payload object (ready to be serialized and sent to ReadMe)
        """
        payload = {
            "group": self.grouping_function(request),
            "clientIPAddress": request.remote_addr,
            "development": self.development_mode,
            "request": {
                "log": {
                    "creator": {
                        "name": __name__,
                        "version": pkg_resources.require("readme_metrics")[0].version,
                        "comment": sys.version,
                    },
                    "entries": [
                        {
                            "pageref": request.base_url,
                            "startedDateTime": request.rm_start_dt,
                            "time": int(time.time() * 1000) - request.rm_start_ts,
                            "request": self._build_request_payload(request),
                            "response": self._build_response_payload(response),
                        }
                    ],
                }
            },
        }

        return payload

    def _build_request_payload(self, request: Request) -> dict:
        """Wraps the request portion of the payload

        Args:
            request (Request): Request object containing the response information

        Returns:
            dict: Wrapped request payload
        """
        post_data = {}
        headers = None

        if self.blacklist:
            headers = util_exclude_keys(request.headers, self.blacklist)
        elif self.whitelist:
            headers = util_filter_keys(request.headers, self.whitelist)
        else:
            headers = request.headers

        if request.content_length is not None and request.content_length > 0:

            body = request.rm_body.decode("utf-8") or ""

            try:
                json_object = json.loads(body)

                if self.blacklist:
                    body = util_exclude_keys(json_object, self.blacklist)
                elif self.whitelist:
                    body = util_filter_keys(json_object, self.whitelist)

                post_data["mimeType"] = "application/json"
                post_data["text"] = body
            except ValueError as e:
                post_data["params"] = [body]

                if request.content_type:
                    post_data["mimeType"] = request.content_type
                else:
                    post_data["mimeType"] = "text/html"

        hdr_items = []
        for k, v in headers.items():
            hdr_items.append({"name": k, "value": v})

        qs_items = []
        qs_dict = dict(parse.parse_qsl(request.query_string.decode("utf-8")))

        for k, v in qs_dict.items():
            qs_items.append({"name": k, "value": v})

        return {
            "method": request.method,
            "url": request.base_url,
            "httpVersion": request.environ["SERVER_PROTOCOL"],
            "headers": hdr_items,
            "queryString": qs_items,
            **post_data,
        }

    def _build_response_payload(self, response: ResponseInfoWrapper) -> dict:
        """Wraps the response portion of the payload

        Args:
            response (ResponseInfoWrapper): containing the response information

        Returns:
            dict: Wrapped response payload
        """
        if self.blacklist:
            headers = util_exclude_keys(response.headers, self.blacklist)
        elif self.whitelist:
            headers = util_filter_keys(response.headers, self.whitelist)
        else:
            headers = response.headers

        body = response.body

        try:
            json_object = json.loads(body)

            if self.blacklist:
                body = util_exclude_keys(json_object, self.blacklist)
            elif self.whitelist:
                body = util_filter_keys(json_object, self.whitelist)
        except ValueError:
            pass

        hdr_items = []
        for k, v in headers.items():
            hdr_items.append({"name": k, "value": v})

        status_code = int(response.status.split(" ")[0])
        status_text = response.status.replace(str(status_code) + " ", "")

        return {
            "status": status_code,
            "statusText": status_text or "",
            "headers": hdr_items,  # headers.items(),
            "content": {
                "text": body,
                "size": response.content_length,
                "mimeType": response.content_type,
            },
        }
