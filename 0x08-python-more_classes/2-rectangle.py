#!/usr/bin/python3


class Rectangle:
    """Class that defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initialization of the rectangle with optional width and height"""
        self.width = width
        self.height = height

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

    @property
                                                                                                                                            def height(self):
                                                                                                                                                        """Height property getter"""
                                                                                                                                                                return self.__height

                                                                                                                                                                @height.setter
                                                                                                                                                                    def height(self, value):
                                                                                                                                                                                """Height property setter: validates height"""
                                                                                                                                                                                        if not isinstance(value, int):
                                                                                                                                                                                                        raise TypeError("height must be an integer")
                                                                                                                                                                                                            if value < 0:
                                                                                                                                                                                                                            raise ValueError("height must be >= 0")
                                                                                                                                                                                                                                self.__height = value

                                                                                                                                                                                                                                    def area(self):
                                                                                                                                                                                                                                                """Public instance method to calculate the area of the rectangle"""
                                                                                                                                                                                                                                                        return self.__width * self.__height

                                                                                                                                                                                                                                                        def perimeter(self):
                                                                                                                                                                                                                                                                    """Public instance method to calculate the perimeter of the rectangle
                                                                                                                                                                                                                                                                            If width or height is 0, return 0 for the perimeter."""
                                                                                                                                                                                                                                                                                    if self.__width == 0 or self.__height == 0:
                                                                                                                                                                                                                                                                                                    return 0
                                                                                                                                                                                                                                                                                                        return 2 * (self.__width + self.__height)
