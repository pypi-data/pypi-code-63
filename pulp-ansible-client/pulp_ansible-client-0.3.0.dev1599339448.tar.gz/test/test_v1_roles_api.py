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

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.api.v1_roles_api import V1RolesApi  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException


class TestV1RolesApi(unittest.TestCase):
    """V1RolesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_ansible.api.v1_roles_api.V1RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get

        """
        pass


if __name__ == '__main__':
    unittest.main()
