#!/usr/bin/python3
"""
This module contains the definition of the Rectangle class,
which models a rectangle with width and height.
"""

class Rectangle:
    """Class that defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initialization of the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """method that returns value of the height

        Returns:
            height of the rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines height

        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width property setter: validates width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
