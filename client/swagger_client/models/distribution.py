# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Distribution(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cpe_uri=None, architecture=None, latest_version=None, maintainer=None, url=None, description=None):
        """
        Distribution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cpe_uri': 'str',
            'architecture': 'str',
            'latest_version': 'Version',
            'maintainer': 'str',
            'url': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'cpe_uri': 'cpeUri',
            'architecture': 'architecture',
            'latest_version': 'latestVersion',
            'maintainer': 'maintainer',
            'url': 'url',
            'description': 'description'
        }

        self._cpe_uri = cpe_uri
        self._architecture = architecture
        self._latest_version = latest_version
        self._maintainer = maintainer
        self._url = url
        self._description = description

    @property
    def cpe_uri(self):
        """
        Gets the cpe_uri of this Distribution.
        The cpe_uri in [cpe format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package.

        :return: The cpe_uri of this Distribution.
        :rtype: str
        """
        return self._cpe_uri

    @cpe_uri.setter
    def cpe_uri(self, cpe_uri):
        """
        Sets the cpe_uri of this Distribution.
        The cpe_uri in [cpe format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package.

        :param cpe_uri: The cpe_uri of this Distribution.
        :type: str
        """

        self._cpe_uri = cpe_uri

    @property
    def architecture(self):
        """
        Gets the architecture of this Distribution.
        The CPU architecture for which packages in this distribution channel were built

        :return: The architecture of this Distribution.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this Distribution.
        The CPU architecture for which packages in this distribution channel were built

        :param architecture: The architecture of this Distribution.
        :type: str
        """
        allowed_values = ["UNKNOWN", "X86", "X64"]
        if architecture not in allowed_values:
            raise ValueError(
                "Invalid value for `architecture` ({0}), must be one of {1}"
                .format(architecture, allowed_values)
            )

        self._architecture = architecture

    @property
    def latest_version(self):
        """
        Gets the latest_version of this Distribution.
        The latest available version of this package in this distribution channel.

        :return: The latest_version of this Distribution.
        :rtype: Version
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """
        Sets the latest_version of this Distribution.
        The latest available version of this package in this distribution channel.

        :param latest_version: The latest_version of this Distribution.
        :type: Version
        """

        self._latest_version = latest_version

    @property
    def maintainer(self):
        """
        Gets the maintainer of this Distribution.
        A freeform string denoting the maintainer of this package.

        :return: The maintainer of this Distribution.
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        """
        Sets the maintainer of this Distribution.
        A freeform string denoting the maintainer of this package.

        :param maintainer: The maintainer of this Distribution.
        :type: str
        """

        self._maintainer = maintainer

    @property
    def url(self):
        """
        Gets the url of this Distribution.
        The distribution channel-specific homepage for this package.

        :return: The url of this Distribution.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Distribution.
        The distribution channel-specific homepage for this package.

        :param url: The url of this Distribution.
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """
        Gets the description of this Distribution.
        The distribution channel-specific description of this package.

        :return: The description of this Distribution.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Distribution.
        The distribution channel-specific description of this package.

        :param description: The description of this Distribution.
        :type: str
        """

        self._description = description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
