#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary description with a simple data structure
        (list, dictionary, string, integer and boolean) for JSON serialization of a Student object.
        If attrs is a list of strings, only those attributes will be included.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a given json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
