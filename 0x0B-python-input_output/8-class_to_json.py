#!/usr/bin/python3
"""contains the "class_to_json" function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structures
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
