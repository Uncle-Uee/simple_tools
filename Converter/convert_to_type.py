"""
Created By: Ubaidullah Effendi-Emjedi
Date: 27 October 2019
"""

import json


def type_conversion(value=""):
    """
    Convert a String to its Correct Type using the Builtin Json Package.
    :param value: A string Value to Convert.
    :return:
    """
    try:
        value = "false" if value == "False" else "true" if value == "True" else "" if value == "null" else value
        return json.loads(value)
    except ValueError:
        return value


def types_conversion(values=[]):
    """
    Convert a List of Values to there Correct Types using the Builtin Json Package.
    :param values: A string Value to Convert.
    :return:
    """
    for value in values:
        try:
            value = "false" if value == "False" else "true" if value == "True" else "" if value == "null" else value
            yield json.loads(value)
        except ValueError:
            yield value


def adv_type_conversion(value="", allow_empty_string=True, allow_null_value=True):
    """
        Convert a String to its Correct Type using the Builtin Json Package.
        :param value: A string Value to Convert.
        :param allow_empty_string: Allow empty string Values.
        :param allow_null_value: Allow null values.
        :return:
        """
    try:
        value = "false" if value == "False" else "true" if value == "True" else "null" if value == "" and not allow_empty_string else "" if value == "null" and not allow_null_value else value
        return json.loads(value)
    except ValueError:
        return value
