# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_container.configuration import Configuration


class ContainerContainerRemoteResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'name': 'str',
        'url': 'str',
        'ca_cert': 'str',
        'client_cert': 'str',
        'client_key': 'str',
        'tls_validation': 'bool',
        'proxy_url': 'str',
        'username': 'str',
        'password': 'str',
        'pulp_last_updated': 'datetime',
        'download_concurrency': 'int',
        'policy': 'PolicyEnum',
        'upstream_name': 'str',
        'include_tags': 'list[str]',
        'exclude_tags': 'list[str]'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'name': 'name',
        'url': 'url',
        'ca_cert': 'ca_cert',
        'client_cert': 'client_cert',
        'client_key': 'client_key',
        'tls_validation': 'tls_validation',
        'proxy_url': 'proxy_url',
        'username': 'username',
        'password': 'password',
        'pulp_last_updated': 'pulp_last_updated',
        'download_concurrency': 'download_concurrency',
        'policy': 'policy',
        'upstream_name': 'upstream_name',
        'include_tags': 'include_tags',
        'exclude_tags': 'exclude_tags'
    }

    def __init__(self, pulp_href=None, pulp_created=None, name=None, url=None, ca_cert=None, client_cert=None, client_key=None, tls_validation=None, proxy_url=None, username=None, password=None, pulp_last_updated=None, download_concurrency=None, policy=None, upstream_name=None, include_tags=None, exclude_tags=None, local_vars_configuration=None):  # noqa: E501
        """ContainerContainerRemoteResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._name = None
        self._url = None
        self._ca_cert = None
        self._client_cert = None
        self._client_key = None
        self._tls_validation = None
        self._proxy_url = None
        self._username = None
        self._password = None
        self._pulp_last_updated = None
        self._download_concurrency = None
        self._policy = None
        self._upstream_name = None
        self._include_tags = None
        self._exclude_tags = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.name = name
        self.url = url
        self.ca_cert = ca_cert
        self.client_cert = client_cert
        self.client_key = client_key
        if tls_validation is not None:
            self.tls_validation = tls_validation
        self.proxy_url = proxy_url
        self.username = username
        self.password = password
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        if download_concurrency is not None:
            self.download_concurrency = download_concurrency
        if policy is not None:
            self.policy = policy
        self.upstream_name = upstream_name
        self.include_tags = include_tags
        self.exclude_tags = exclude_tags

    @property
    def pulp_href(self):
        """Gets the pulp_href of this ContainerContainerRemoteResponse.  # noqa: E501


        :return: The pulp_href of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this ContainerContainerRemoteResponse.


        :param pulp_href: The pulp_href of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this ContainerContainerRemoteResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this ContainerContainerRemoteResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def name(self):
        """Gets the name of this ContainerContainerRemoteResponse.  # noqa: E501

        A unique name for this remote.  # noqa: E501

        :return: The name of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContainerContainerRemoteResponse.

        A unique name for this remote.  # noqa: E501

        :param name: The name of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this ContainerContainerRemoteResponse.  # noqa: E501

        The URL of an external content source.  # noqa: E501

        :return: The url of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContainerContainerRemoteResponse.

        The URL of an external content source.  # noqa: E501

        :param url: The url of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def ca_cert(self):
        """Gets the ca_cert of this ContainerContainerRemoteResponse.  # noqa: E501

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :return: The ca_cert of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._ca_cert

    @ca_cert.setter
    def ca_cert(self, ca_cert):
        """Sets the ca_cert of this ContainerContainerRemoteResponse.

        A PEM encoded CA certificate used to validate the server certificate presented by the remote server.  # noqa: E501

        :param ca_cert: The ca_cert of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._ca_cert = ca_cert

    @property
    def client_cert(self):
        """Gets the client_cert of this ContainerContainerRemoteResponse.  # noqa: E501

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :return: The client_cert of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this ContainerContainerRemoteResponse.

        A PEM encoded client certificate used for authentication.  # noqa: E501

        :param client_cert: The client_cert of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._client_cert = client_cert

    @property
    def client_key(self):
        """Gets the client_key of this ContainerContainerRemoteResponse.  # noqa: E501

        A PEM encoded private key used for authentication.  # noqa: E501

        :return: The client_key of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this ContainerContainerRemoteResponse.

        A PEM encoded private key used for authentication.  # noqa: E501

        :param client_key: The client_key of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._client_key = client_key

    @property
    def tls_validation(self):
        """Gets the tls_validation of this ContainerContainerRemoteResponse.  # noqa: E501

        If True, TLS peer validation must be performed.  # noqa: E501

        :return: The tls_validation of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: bool
        """
        return self._tls_validation

    @tls_validation.setter
    def tls_validation(self, tls_validation):
        """Sets the tls_validation of this ContainerContainerRemoteResponse.

        If True, TLS peer validation must be performed.  # noqa: E501

        :param tls_validation: The tls_validation of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: bool
        """

        self._tls_validation = tls_validation

    @property
    def proxy_url(self):
        """Gets the proxy_url of this ContainerContainerRemoteResponse.  # noqa: E501

        The proxy URL. Format: scheme://user:password@host:port  # noqa: E501

        :return: The proxy_url of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this ContainerContainerRemoteResponse.

        The proxy URL. Format: scheme://user:password@host:port  # noqa: E501

        :param proxy_url: The proxy_url of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def username(self):
        """Gets the username of this ContainerContainerRemoteResponse.  # noqa: E501

        The username to be used for authentication when syncing.  # noqa: E501

        :return: The username of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ContainerContainerRemoteResponse.

        The username to be used for authentication when syncing.  # noqa: E501

        :param username: The username of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this ContainerContainerRemoteResponse.  # noqa: E501

        The password to be used for authentication when syncing.  # noqa: E501

        :return: The password of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ContainerContainerRemoteResponse.

        The password to be used for authentication when syncing.  # noqa: E501

        :param password: The password of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this ContainerContainerRemoteResponse.  # noqa: E501

        Timestamp of the most recent update of the remote.  # noqa: E501

        :return: The pulp_last_updated of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this ContainerContainerRemoteResponse.

        Timestamp of the most recent update of the remote.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def download_concurrency(self):
        """Gets the download_concurrency of this ContainerContainerRemoteResponse.  # noqa: E501

        Total number of simultaneous connections.  # noqa: E501

        :return: The download_concurrency of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: int
        """
        return self._download_concurrency

    @download_concurrency.setter
    def download_concurrency(self, download_concurrency):
        """Sets the download_concurrency of this ContainerContainerRemoteResponse.

        Total number of simultaneous connections.  # noqa: E501

        :param download_concurrency: The download_concurrency of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                download_concurrency is not None and download_concurrency < 1):  # noqa: E501
            raise ValueError("Invalid value for `download_concurrency`, must be a value greater than or equal to `1`")  # noqa: E501

        self._download_concurrency = download_concurrency

    @property
    def policy(self):
        """Gets the policy of this ContainerContainerRemoteResponse.  # noqa: E501

                 immediate - All manifests and blobs are downloaded and saved during a sync.         on_demand - Only tags and manifests are downloaded. Blobs are not                     downloaded until they are requested for the first time by a client.         streamed - Blobs are streamed to the client with every request and never saved.           # noqa: E501

        :return: The policy of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: PolicyEnum
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this ContainerContainerRemoteResponse.

                 immediate - All manifests and blobs are downloaded and saved during a sync.         on_demand - Only tags and manifests are downloaded. Blobs are not                     downloaded until they are requested for the first time by a client.         streamed - Blobs are streamed to the client with every request and never saved.           # noqa: E501

        :param policy: The policy of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: PolicyEnum
        """

        self._policy = policy

    @property
    def upstream_name(self):
        """Gets the upstream_name of this ContainerContainerRemoteResponse.  # noqa: E501

        Name of the upstream repository  # noqa: E501

        :return: The upstream_name of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: str
        """
        return self._upstream_name

    @upstream_name.setter
    def upstream_name(self, upstream_name):
        """Sets the upstream_name of this ContainerContainerRemoteResponse.

        Name of the upstream repository  # noqa: E501

        :param upstream_name: The upstream_name of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and upstream_name is None:  # noqa: E501
            raise ValueError("Invalid value for `upstream_name`, must not be `None`")  # noqa: E501

        self._upstream_name = upstream_name

    @property
    def include_tags(self):
        """Gets the include_tags of this ContainerContainerRemoteResponse.  # noqa: E501

                     A list of tags to include during sync.             Wildcards *, ? are recognized.             'include_tags' is evaluated before 'exclude_tags'.               # noqa: E501

        :return: The include_tags of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_tags

    @include_tags.setter
    def include_tags(self, include_tags):
        """Sets the include_tags of this ContainerContainerRemoteResponse.

                     A list of tags to include during sync.             Wildcards *, ? are recognized.             'include_tags' is evaluated before 'exclude_tags'.               # noqa: E501

        :param include_tags: The include_tags of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: list[str]
        """

        self._include_tags = include_tags

    @property
    def exclude_tags(self):
        """Gets the exclude_tags of this ContainerContainerRemoteResponse.  # noqa: E501

                     A list of tags to exclude during sync.             Wildcards *, ? are recognized.             'exclude_tags' is evaluated after 'include_tags'.               # noqa: E501

        :return: The exclude_tags of this ContainerContainerRemoteResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_tags

    @exclude_tags.setter
    def exclude_tags(self, exclude_tags):
        """Sets the exclude_tags of this ContainerContainerRemoteResponse.

                     A list of tags to exclude during sync.             Wildcards *, ? are recognized.             'exclude_tags' is evaluated after 'include_tags'.               # noqa: E501

        :param exclude_tags: The exclude_tags of this ContainerContainerRemoteResponse.  # noqa: E501
        :type: list[str]
        """

        self._exclude_tags = exclude_tags

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
        if not isinstance(other, ContainerContainerRemoteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerContainerRemoteResponse):
            return True

        return self.to_dict() != other.to_dict()
