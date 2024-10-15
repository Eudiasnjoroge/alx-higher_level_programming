#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the number of characters added.
    Args:
        filename (str): The name ofthe file to append to. If the file does not exist, it will be created.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
