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


class LinkSignable(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _type=None, name=None, command=None, materials=None, products=None,
            byproducts=None, environment=None):
        """
        BuildDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            "_type" : "str",
            "name" : "str",
            "command" : "str",
            "materials": "dict(str, dict(str, str))",
            "products": "dict(str, dict(str, str))",
            "byproducts": "dict(str, str)",
            "environment": "dict(str, str)",
        }

        self.attribute_map = {
            "_type" : "_type",
            "name" : "name",
            "command" : "command",
            "materials": "materials",
            "products": "products",
            "byproducts": "byproducts",
            "environment": "environment",
        }
        self.__type = "link"
        self._name = name
        self._command = command
        self._materials = materials
        self._products = products
        self._byproducts = byproducts
        self._environment = environment

    @property
    def _type(self):
        """
        Gets the _type of this BuildDetails.
        The actual _type

        :return: The _type of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self.__type

    @_type.setter
    def _type(self, _type):
        """
        Sets the _type of this BuildDetails.
        The actual _type

        :param _type: The _type of this BuildDetails.
        :type: BuildProvenance
        """

        self.__type = _type

    @property
    def name(self):
        """
        Gets the name of this BuildDetails.
        The actual name

        :return: The name of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildDetails.
        The actual name

        :param name: The name of this BuildDetails.
        :type: BuildProvenance
        """

        self._name = name

    @property
    def command(self):
        """
        Gets the command of this BuildDetails.
        The actual command

        :return: The command of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this BuildDetails.
        The actual command

        :param command: The command of this BuildDetails.
        :type: BuildProvenance
        """

        self._command = command

    @property
    def materials(self):
        """
        Gets the materials of this BuildDetails.
        The actual materials

        :return: The materials of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """
        Sets the materials of this BuildDetails.
        The actual materials

        :param materials: The materials of this BuildDetails.
        :type: BuildProvenance
        """

        self._materials = materials

    @property
    def products(self):
        """
        Gets the products of this BuildDetails.
        The actual products

        :return: The products of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this BuildDetails.
        The actual products

        :param products: The products of this BuildDetails.
        :type: BuildProvenance
        """

        self._products = products


    @property
    def byproducts(self):
        """
        Gets the byproducts of this BuildDetails.
        The actual byproducts

        :return: The byproducts of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self._byproducts

    @byproducts.setter
    def byproducts(self, signed):
        """
        Sets the byproducts of this BuildDetails.
        The actual byproducts

        :param byproducts: The signed of this BuildDetails.
        :type: BuildProvenance
        """

        self._byproducts = signed

    @property
    def environment(self):
        """
        Gets the environment of this BuildDetails.
        The actual environment

        :return: The environment of this BuildDetails.
        :rtype: BuildProvenance
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this BuildDetails.
        The actual environment

        :param environment: The environment of this BuildDetails.
        :type: BuildProvenance
        """

        self._environment = environment

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
