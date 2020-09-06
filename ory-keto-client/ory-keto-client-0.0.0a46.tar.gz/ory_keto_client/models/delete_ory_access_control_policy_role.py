# coding: utf-8

"""
    ORY Keto

    A cloud native access control server providing best-practice patterns (RBAC, ABAC, ACL, AWS IAM Policies, Kubernetes Roles, ...) via REST APIs.  # noqa: E501

    The version of the OpenAPI document: v0.0.0-alpha.37
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_keto_client.configuration import Configuration


class DeleteOryAccessControlPolicyRole(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'flavor': 'str',
        'id': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'id': 'id'
    }

    def __init__(self, flavor=None, id=None, local_vars_configuration=None):  # noqa: E501
        """DeleteOryAccessControlPolicyRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._flavor = None
        self._id = None
        self.discriminator = None

        self.flavor = flavor
        self.id = id

    @property
    def flavor(self):
        """Gets the flavor of this DeleteOryAccessControlPolicyRole.  # noqa: E501

        The ORY Access Control Policy flavor. Can be \"regex\", \"glob\", and \"exact\".  in: path  # noqa: E501

        :return: The flavor of this DeleteOryAccessControlPolicyRole.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this DeleteOryAccessControlPolicyRole.

        The ORY Access Control Policy flavor. Can be \"regex\", \"glob\", and \"exact\".  in: path  # noqa: E501

        :param flavor: The flavor of this DeleteOryAccessControlPolicyRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and flavor is None:  # noqa: E501
            raise ValueError("Invalid value for `flavor`, must not be `None`")  # noqa: E501

        self._flavor = flavor

    @property
    def id(self):
        """Gets the id of this DeleteOryAccessControlPolicyRole.  # noqa: E501

        The ID of the ORY Access Control Policy Role. in: path  # noqa: E501

        :return: The id of this DeleteOryAccessControlPolicyRole.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteOryAccessControlPolicyRole.

        The ID of the ORY Access Control Policy Role. in: path  # noqa: E501

        :param id: The id of this DeleteOryAccessControlPolicyRole.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteOryAccessControlPolicyRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteOryAccessControlPolicyRole):
            return True

        return self.to_dict() != other.to_dict()
