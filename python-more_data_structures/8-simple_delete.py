#!/usr/bin/python3
def simple_delete(a_dict, key):
    try:
        del a_dict[key]
        return a_dict
    except KeyError:
        return a_dict
