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


class PostMissionQueues(object):
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
        'message': 'str',
        'mission_id': 'str',
        'parameters': 'list[object]',
        'priority': 'int'
    }

    attribute_map = {
        'message': 'message',
        'mission_id': 'mission_id',
        'parameters': 'parameters',
        'priority': 'priority'
    }

    def __init__(self, message=None, mission_id=None, parameters=None, priority=None):  # noqa: E501
        """PostMissionQueues - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._mission_id = None
        self._parameters = None
        self._priority = None
        self.discriminator = None
        if message is not None:
            self.message = message
        self.mission_id = mission_id
        if parameters is not None:
            self.parameters = parameters
        if priority is not None:
            self.priority = priority

    @property
    def message(self):
        """Gets the message of this PostMissionQueues.  # noqa: E501

        Max length: 200  # noqa: E501

        :return: The message of this PostMissionQueues.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PostMissionQueues.

        Max length: 200  # noqa: E501

        :param message: The message of this PostMissionQueues.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def mission_id(self):
        """Gets the mission_id of this PostMissionQueues.  # noqa: E501


        :return: The mission_id of this PostMissionQueues.  # noqa: E501
        :rtype: str
        """
        return self._mission_id

    @mission_id.setter
    def mission_id(self, mission_id):
        """Sets the mission_id of this PostMissionQueues.


        :param mission_id: The mission_id of this PostMissionQueues.  # noqa: E501
        :type: str
        """
        if mission_id is None:
            raise ValueError("Invalid value for `mission_id`, must not be `None`")  # noqa: E501

        self._mission_id = mission_id

    @property
    def parameters(self):
        """Gets the parameters of this PostMissionQueues.  # noqa: E501


        :return: The parameters of this PostMissionQueues.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PostMissionQueues.


        :param parameters: The parameters of this PostMissionQueues.  # noqa: E501
        :type: list[object]
        """

        self._parameters = parameters

    @property
    def priority(self):
        """Gets the priority of this PostMissionQueues.  # noqa: E501


        :return: The priority of this PostMissionQueues.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PostMissionQueues.


        :param priority: The priority of this PostMissionQueues.  # noqa: E501
        :type: int
        """

        self._priority = priority

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
        if issubclass(PostMissionQueues, dict):
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
        if not isinstance(other, PostMissionQueues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
