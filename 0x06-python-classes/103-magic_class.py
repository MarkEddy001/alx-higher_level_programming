#!/usr/bin/python3
""" Magic Class """
import math


class MagicClass:
    """ circle class """

    def __init__(self, radius=0) -> None:
        """ create the class object """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ find the area of a circle """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ find the circumference of a circle"""
        return math.pi * 2 * self.__radius
