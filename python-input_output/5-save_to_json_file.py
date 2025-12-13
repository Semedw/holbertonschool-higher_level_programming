#!/usr/bin/python3
"""
save object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    inside the function
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        text = json.dump(my_obj, f)
