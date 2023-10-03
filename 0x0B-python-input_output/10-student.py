#!/usr/bin/python3

"""Defines a class student"""
class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the students details

        Args:
            first_name (str): the students first name
            last_name (str): the students last name
            age (int): the students name

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """finding the dictionary rep of students.

        attrs = the list of strings representing the attributes
        only included in the list

        Args:
        attrs (list): list of attributes in the list
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
