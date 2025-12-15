#!/usr/bin/python3
"""
basic serialization
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    inside the serialize function
    """
    with open(filename, mode='wb') as file:
        pickle.dump(data, filename)


def load_and_deserialize(filename):
    """
    inside the load function
    """
    with open(filename, mode='rb') as file:
        result = pickle.load(filename)
    return result
