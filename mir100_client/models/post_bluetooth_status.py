# coding: utf-8

"""
    MIR100 Rest Interface

    Automatically converted from v270 pdf  # noqa: E501

    OpenAPI spec version: 2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PostBluetoothStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'module_guid': 'str'
    }

    attribute_map = {
        'module_guid': 'module_guid'
    }

    def __init__(self, module_guid=None):  # noqa: E501
        """PostBluetoothStatus - a model defined in Swagger"""  # noqa: E501
        self._module_guid = None
        self.discriminator = None
        self.module_guid = module_guid

    @property
    def module_guid(self):
        """Gets the module_guid of this PostBluetoothStatus.  # noqa: E501


        :return: The module_guid of this PostBluetoothStatus.  # noqa: E501
        :rtype: str
        """
        return self._module_guid

    @module_guid.setter
    def module_guid(self, module_guid):
        """Sets the module_guid of this PostBluetoothStatus.


        :param module_guid: The module_guid of this PostBluetoothStatus.  # noqa: E501
        :type: str
        """
        if module_guid is None:
            raise ValueError("Invalid value for `module_guid`, must not be `None`")  # noqa: E501

        self._module_guid = module_guid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PostBluetoothStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostBluetoothStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other