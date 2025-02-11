#!/usr/bin/python3
'''Module for rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''method for validating the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and Value <= 0:
            raise ValueError("{} must be > 0".format(name))
