#!/usr/bin/python3
"""
basic serialization
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    inside the serialize function
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    inside the load function
    """
    with open(filename, 'rb') as file:
        try:
            result = pickle.load(file)
        except AttributeError:
            result = []
    return result
