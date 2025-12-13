#!/usr/bin/python3
"""
load, add, and save
"""

import json


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

argv = sys.argv[1:]
save(argv)
