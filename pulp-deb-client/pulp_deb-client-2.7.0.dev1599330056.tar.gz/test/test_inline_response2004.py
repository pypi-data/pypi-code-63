# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_deb
from pulpcore.client.pulp_deb.models.inline_response2004 import InlineResponse2004  # noqa: E501
from pulpcore.client.pulp_deb.rest import ApiException

class TestInlineResponse2004(unittest.TestCase):
    """InlineResponse2004 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2004
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_deb.models.inline_response2004.InlineResponse2004()  # noqa: E501
        if include_optional :
            return InlineResponse2004(
                count = 123, 
                next = '0', 
                previous = '0', 
                results = [
                    pulpcore.client.pulp_deb.models.deb/package_release_component_response.deb.PackageReleaseComponentResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        package = '0', 
                        release_component = '0', )
                    ]
            )
        else :
            return InlineResponse2004(
        )

    def testInlineResponse2004(self):
        """Test InlineResponse2004"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
