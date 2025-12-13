#!/usr/bin/python3
"""
class to json
"""

import json


def class_to_json(obj):
    """
    inside the function
    """
    dict_obj = obj.__dict__
    return json.dumps(dict_obj))
