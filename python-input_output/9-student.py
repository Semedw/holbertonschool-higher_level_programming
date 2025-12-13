#!/usr/bin/python3
"""
student to json
"""


class Student:
    """
    inside the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        inside the init method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        inside the public function
        """
        d_json = {}
        d_json['first_name'] = self.first_name
        d_json['last_name'] = self.first_name
        d_json['age'] = self.age
        return d_json
