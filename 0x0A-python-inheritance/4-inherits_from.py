#!/usr/bin/python3
"""module for inherits_from method"""


def inherits_from(obj, a_class):
    """determines if the object is an instance of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
