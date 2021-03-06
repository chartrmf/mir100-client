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


class Position(object):
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
        'orientation': 'float',
        'x': 'float',
        'y': 'float'
    }

    attribute_map = {
        'orientation': 'orientation',
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, orientation=None, x=None, y=None):  # noqa: E501
        """Position - a model defined in Swagger"""  # noqa: E501
        self._orientation = None
        self._x = None
        self._y = None
        self.discriminator = None
        if orientation is not None:
            self.orientation = orientation
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def orientation(self):
        """Gets the orientation of this Position.  # noqa: E501

        The orientation of the current position of the robot  # noqa: E501

        :return: The orientation of this Position.  # noqa: E501
        :rtype: float
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this Position.

        The orientation of the current position of the robot  # noqa: E501

        :param orientation: The orientation of this Position.  # noqa: E501
        :type: float
        """

        self._orientation = orientation

    @property
    def x(self):
        """Gets the x of this Position.  # noqa: E501

        The x-coordinate of the current position of the robot  # noqa: E501

        :return: The x of this Position.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Position.

        The x-coordinate of the current position of the robot  # noqa: E501

        :param x: The x of this Position.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this Position.  # noqa: E501

        The y-coordinate of the current position of the robot  # noqa: E501

        :return: The y of this Position.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Position.

        The y-coordinate of the current position of the robot  # noqa: E501

        :param y: The y of this Position.  # noqa: E501
        :type: float
        """

        self._y = y

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
        if issubclass(Position, dict):
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
        if not isinstance(other, Position):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
