#!/usr/bin/python3
"""
load, add, and save
"""

import sys
from pathlib import Path

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

if Path(add_item.json).exists():
    argv = load(add_items.json)
else:
    argv = []

argv += sys.argv[1:]
save(argv, 'add_item.json')
