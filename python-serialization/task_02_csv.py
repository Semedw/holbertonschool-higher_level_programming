#!/usr/bin/python3
"""
converting csv to json
"""
import csv
import json


def convert_to_json(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
    with open('data.json', mode='w', encoding='utf-8') as jsonfile:
        try:
            json.dump(data, jsonfile)
            return True
        except Exception:
            return False
