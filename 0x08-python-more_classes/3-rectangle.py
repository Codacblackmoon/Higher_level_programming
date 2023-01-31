#!/usr/bin/python3

class Rectanglie:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
                             
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, widthValue):
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, HeightValue:
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        width = self.__width
        height = self.__height
        if width == 0 or height == 0
            return 0
        return (width + height) * 2

    def __str__(self):
        width = self.__width
        height = self.__height
        string = ""
        if width == 0 or height == 0:
            return strin
        for r in range(height):
            for c in range(width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]


