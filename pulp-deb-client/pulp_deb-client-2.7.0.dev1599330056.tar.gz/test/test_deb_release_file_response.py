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
from pulpcore.client.pulp_deb.models.deb_release_file_response import DebReleaseFileResponse  # noqa: E501
from pulpcore.client.pulp_deb.rest import ApiException

class TestDebReleaseFileResponse(unittest.TestCase):
    """DebReleaseFileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DebReleaseFileResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_deb.models.deb_release_file_response.DebReleaseFileResponse()  # noqa: E501
        if include_optional :
            return DebReleaseFileResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                artifacts = None, 
                codename = '0', 
                suite = '0', 
                distribution = '0', 
                relative_path = '0'
            )
        else :
            return DebReleaseFileResponse(
                artifacts = None,
                codename = '0',
        )

    def testDebReleaseFileResponse(self):
        """Test DebReleaseFileResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
