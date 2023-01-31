#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, widthValue):
        if type(widthValue) != 0:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, heightValue):
        if type(heightValue) != 0:
            raise TypeError("height must be an integer")
        if heightValue < 0:
            raise ValueError("height must >) 0")
        self.__height = heightValue
