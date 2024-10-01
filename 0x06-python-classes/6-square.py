#!/usr/bin/python3

"""Define a square class"""


class Square:
    """rep... of a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """instantation with size for our object
        initialization
        """
        self.__size = size
        self.position = position

        """private attribute"""
    @property
    def position(self):
        """private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter and position(self, value): to set it"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """make the value of the set meet the standard"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mustbe >= 0")
        self.__size = value

    def area(self):
        """a public method that computes the area of the class object"""
        return (self.__size * self.__size)

    def my_print(self):
        """public instance method that returns the current square area"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for item in range(self.__size):
            [print(" ", end='')for item in range(0, self.__position[0])]
            [print("#", end='')for k in range(0, self.__size)]
            print('')
