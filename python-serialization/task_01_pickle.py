#!/usr/bin/python3
"""
pickling custom classes
"""

import pickle


class CustomObject:
    """
    inside the class
    """

    def __init__(self, name:str, age:int, is_student:bool):
        """
        inside the init file
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        inside the display func
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            try:
                deserialized_list = pickle.load(file)
            except Exception:
                continue
        return deserialized_list
