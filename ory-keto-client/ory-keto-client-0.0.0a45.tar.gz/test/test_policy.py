# coding: utf-8

"""
    ORY Keto

    A cloud native access control server providing best-practice patterns (RBAC, ABAC, ACL, AWS IAM Policies, Kubernetes Roles, ...) via REST APIs.  # noqa: E501

    The version of the OpenAPI document: v0.0.0-alpha.1
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ory_keto_client
from ory_keto_client.models.policy import Policy  # noqa: E501
from ory_keto_client.rest import ApiException


class TestPolicy(unittest.TestCase):
    """Policy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPolicy(self):
        """Test Policy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ory_keto_client.models.policy.Policy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
