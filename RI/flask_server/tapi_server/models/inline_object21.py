# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_getoamjob_input import TapiOamGetoamjobInput  # noqa: F401,E501
from tapi_server import util


class InlineObject21(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject21 - a model defined in OpenAPI

        :param input: The input of this InlineObject21.  # noqa: E501
        :type input: TapiOamGetoamjobInput
        """
        self.openapi_types = {
            'input': TapiOamGetoamjobInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject21':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_21 of this InlineObject21.  # noqa: E501
        :rtype: InlineObject21
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject21.


        :return: The input of this InlineObject21.
        :rtype: TapiOamGetoamjobInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject21.


        :param input: The input of this InlineObject21.
        :type input: TapiOamGetoamjobInput
        """

        self._input = input
