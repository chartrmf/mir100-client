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


class PutStatus(object):
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
        'answer': 'str',
        'clear_error': 'bool',
        '_datetime': 'datetime',
        'guid': 'str',
        'map_id': 'str',
        'mode_id': 'int',
        'name': 'str',
        'position': 'object',
        'serial_number': 'str',
        'state_id': 'int',
        'web_session_id': 'str'
    }

    attribute_map = {
        'answer': 'answer',
        'clear_error': 'clear_error',
        '_datetime': 'datetime',
        'guid': 'guid',
        'map_id': 'map_id',
        'mode_id': 'mode_id',
        'name': 'name',
        'position': 'position',
        'serial_number': 'serial_number',
        'state_id': 'state_id',
        'web_session_id': 'web_session_id'
    }

    def __init__(self, answer=None, clear_error=None, _datetime=None, guid=None, map_id=None, mode_id=None, name=None, position=None, serial_number=None, state_id=None, web_session_id=None):  # noqa: E501
        """PutStatus - a model defined in Swagger"""  # noqa: E501
        self._answer = None
        self._clear_error = None
        self.__datetime = None
        self._guid = None
        self._map_id = None
        self._mode_id = None
        self._name = None
        self._position = None
        self._serial_number = None
        self._state_id = None
        self._web_session_id = None
        self.discriminator = None
        if answer is not None:
            self.answer = answer
        if clear_error is not None:
            self.clear_error = clear_error
        if _datetime is not None:
            self._datetime = _datetime
        if guid is not None:
            self.guid = guid
        if map_id is not None:
            self.map_id = map_id
        if mode_id is not None:
            self.mode_id = mode_id
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if serial_number is not None:
            self.serial_number = serial_number
        if state_id is not None:
            self.state_id = state_id
        if web_session_id is not None:
            self.web_session_id = web_session_id

    @property
    def answer(self):
        """Gets the answer of this PutStatus.  # noqa: E501

        Min length: 1, Max length: 255  # noqa: E501

        :return: The answer of this PutStatus.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this PutStatus.

        Min length: 1, Max length: 255  # noqa: E501

        :param answer: The answer of this PutStatus.  # noqa: E501
        :type: str
        """

        self._answer = answer

    @property
    def clear_error(self):
        """Gets the clear_error of this PutStatus.  # noqa: E501


        :return: The clear_error of this PutStatus.  # noqa: E501
        :rtype: bool
        """
        return self._clear_error

    @clear_error.setter
    def clear_error(self, clear_error):
        """Sets the clear_error of this PutStatus.


        :param clear_error: The clear_error of this PutStatus.  # noqa: E501
        :type: bool
        """

        self._clear_error = clear_error

    @property
    def _datetime(self):
        """Gets the _datetime of this PutStatus.  # noqa: E501


        :return: The _datetime of this PutStatus.  # noqa: E501
        :rtype: datetime
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this PutStatus.


        :param _datetime: The _datetime of this PutStatus.  # noqa: E501
        :type: datetime
        """

        self.__datetime = _datetime

    @property
    def guid(self):
        """Gets the guid of this PutStatus.  # noqa: E501


        :return: The guid of this PutStatus.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PutStatus.


        :param guid: The guid of this PutStatus.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def map_id(self):
        """Gets the map_id of this PutStatus.  # noqa: E501


        :return: The map_id of this PutStatus.  # noqa: E501
        :rtype: str
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this PutStatus.


        :param map_id: The map_id of this PutStatus.  # noqa: E501
        :type: str
        """

        self._map_id = map_id

    @property
    def mode_id(self):
        """Gets the mode_id of this PutStatus.  # noqa: E501

        Choices are: {3, 7}  # noqa: E501

        :return: The mode_id of this PutStatus.  # noqa: E501
        :rtype: int
        """
        return self._mode_id

    @mode_id.setter
    def mode_id(self, mode_id):
        """Sets the mode_id of this PutStatus.

        Choices are: {3, 7}  # noqa: E501

        :param mode_id: The mode_id of this PutStatus.  # noqa: E501
        :type: int
        """

        self._mode_id = mode_id

    @property
    def name(self):
        """Gets the name of this PutStatus.  # noqa: E501

        Min length: 1, Max length: 20  # noqa: E501

        :return: The name of this PutStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutStatus.

        Min length: 1, Max length: 20  # noqa: E501

        :param name: The name of this PutStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this PutStatus.  # noqa: E501


        :return: The position of this PutStatus.  # noqa: E501
        :rtype: object
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PutStatus.


        :param position: The position of this PutStatus.  # noqa: E501
        :type: object
        """

        self._position = position

    @property
    def serial_number(self):
        """Gets the serial_number of this PutStatus.  # noqa: E501


        :return: The serial_number of this PutStatus.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this PutStatus.


        :param serial_number: The serial_number of this PutStatus.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def state_id(self):
        """Gets the state_id of this PutStatus.  # noqa: E501

        Choices are: {3, 4, 11}, State: {Ready, Pause, Manualcontrol}  # noqa: E501

        :return: The state_id of this PutStatus.  # noqa: E501
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this PutStatus.

        Choices are: {3, 4, 11}, State: {Ready, Pause, Manualcontrol}  # noqa: E501

        :param state_id: The state_id of this PutStatus.  # noqa: E501
        :type: int
        """

        self._state_id = state_id

    @property
    def web_session_id(self):
        """Gets the web_session_id of this PutStatus.  # noqa: E501


        :return: The web_session_id of this PutStatus.  # noqa: E501
        :rtype: str
        """
        return self._web_session_id

    @web_session_id.setter
    def web_session_id(self, web_session_id):
        """Sets the web_session_id of this PutStatus.


        :param web_session_id: The web_session_id of this PutStatus.  # noqa: E501
        :type: str
        """

        self._web_session_id = web_session_id

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
        if issubclass(PutStatus, dict):
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
        if not isinstance(other, PutStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
