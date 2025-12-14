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

    def to_json(self, attrs=None):
        """
        inside the public function
        """
        d_json = {}
        result = {}
        s = 0
        d_json['first_name'] = self.first_name
        d_json['last_name'] = self.last_name
        d_json['age'] = self.age
        if attrs is None:
            return d_json
        for key, value in d_json.items():
            if key in attrs:
                result[key] = value
        return result
    
    def reload_from_json(self, json):
        """
        inside the method
        """
        for key, value in json.items():
            setattr(self, key, value)
