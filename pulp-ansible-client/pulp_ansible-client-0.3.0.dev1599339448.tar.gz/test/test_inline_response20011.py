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

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.inline_response20011 import InlineResponse20011  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestInlineResponse20011(unittest.TestCase):
    """InlineResponse20011 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20011
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.inline_response20011.InlineResponse20011()  # noqa: E501
        if include_optional :
            return InlineResponse20011(
                count = 123, 
                next = '0', 
                previous = '0', 
                results = [
                    pulpcore.client.pulp_ansible.models.galaxy_collection_response.GalaxyCollectionResponse(
                        name = '0', 
                        namespace = '0', 
                        href = null, 
                        versions_url = null, )
                    ]
            )
        else :
            return InlineResponse20011(
        )

    def testInlineResponse20011(self):
        """Test InlineResponse20011"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
