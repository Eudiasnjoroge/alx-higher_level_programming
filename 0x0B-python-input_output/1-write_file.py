#!/usr/bin/python3
"""
This modules defines a function that writes a string to a text file(UTF8)
"""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and the returns number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
