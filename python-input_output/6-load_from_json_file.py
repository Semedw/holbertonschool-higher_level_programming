#!/usr/bin/python3
"""
create object from a json file
"""

import json


def load_from_json_file(filename):
    """
    inside the function
    """
    with open(filename, encoding='utf-8')) as f:
        text = f.read()
        obj = json.loads(text)
        return obj
