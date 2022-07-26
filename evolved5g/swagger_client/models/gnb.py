# coding: utf-8

"""
    NEF_Emulator

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GNB(object):
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
        'g_nb_id': 'str',
        'name': 'str',
        'description': 'str',
        'location': 'str',
        'owner_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'g_nb_id': 'gNB_id',
        'name': 'name',
        'description': 'description',
        'location': 'location',
        'owner_id': 'owner_id',
        'id': 'id'
    }

    def __init__(self, g_nb_id=None, name=None, description=None, location=None, owner_id=None, id=None):  # noqa: E501
        """GNB - a model defined in Swagger"""  # noqa: E501
        self._g_nb_id = None
        self._name = None
        self._description = None
        self._location = None
        self._owner_id = None
        self._id = None
        self.discriminator = None
        self.g_nb_id = g_nb_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if location is not None:
            self.location = location
        if owner_id is not None:
            self.owner_id = owner_id
        if id is not None:
            self.id = id

    @property
    def g_nb_id(self):
        """Gets the g_nb_id of this GNB.  # noqa: E501


        :return: The g_nb_id of this GNB.  # noqa: E501
        :rtype: str
        """
        return self._g_nb_id

    @g_nb_id.setter
    def g_nb_id(self, g_nb_id):
        """Sets the g_nb_id of this GNB.


        :param g_nb_id: The g_nb_id of this GNB.  # noqa: E501
        :type: str
        """
        if g_nb_id is None:
            raise ValueError("Invalid value for `g_nb_id`, must not be `None`")  # noqa: E501

        self._g_nb_id = g_nb_id

    @property
    def name(self):
        """Gets the name of this GNB.  # noqa: E501


        :return: The name of this GNB.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GNB.


        :param name: The name of this GNB.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this GNB.  # noqa: E501


        :return: The description of this GNB.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GNB.


        :param description: The description of this GNB.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def location(self):
        """Gets the location of this GNB.  # noqa: E501


        :return: The location of this GNB.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GNB.


        :param location: The location of this GNB.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def owner_id(self):
        """Gets the owner_id of this GNB.  # noqa: E501


        :return: The owner_id of this GNB.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this GNB.


        :param owner_id: The owner_id of this GNB.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def id(self):
        """Gets the id of this GNB.  # noqa: E501


        :return: The id of this GNB.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GNB.


        :param id: The id of this GNB.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(GNB, dict):
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
        if not isinstance(other, GNB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
