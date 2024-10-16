#!/usr/bin/python3
"""modules for function that returns True if object is an instance of the class"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class"""
    return type(obj) == a_class
