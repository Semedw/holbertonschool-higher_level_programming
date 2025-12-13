#!/usr/bin/python3
"""
to json string
"""

import json


def to_json_string(my_obj):
    """
    inside the function
    """
    json_repr = json.dumps(my_obj)
    return json_repr
