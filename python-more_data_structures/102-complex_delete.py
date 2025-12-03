#!/usr/bin/python3
def complex_delete(a_dictionary, val):
    for key, value in a_dictionary.copy().items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
