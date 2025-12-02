#!/usr/bin/python3

def multiple_by_2(a_dict):
    new_dict = {}
    for key, value in a_dict.items():
        new_dict[key] = value * 2
    return new_dict
