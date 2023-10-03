#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base

class Rectangle(Base):
    # Initialize the Rectangle class
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    # Getter for x
    @property
    def x(self):
        return self.__x

    # Setter for x
    @x.setter
    def x(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("x must be a non-negative integer")
        self.__x = value

    # Getter for y
    @property
    def y(self):
        return self.__y

    # Setter for y
    @y.setter
    def y(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("y must be a non-negative integer")
        self.__y = value

    # New area method
    def area(self):
        return self.__width * self.__height

    def display(self):
        # Print y number of newlines
        for _ in range(self.__y):
            print()

        # For each row (height)
        for _ in range(self.__height):
            # Print x number of spaces
            print(' ' * self.__x, end='')

            # Print width number of '#' characters
            print('#' * self.__width)


    # Overridden __str__ method
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

   def update(self, *args, **kwargs):
    attributes = ["id", "width", "height", "x", "y"]
    
    # If args are given, they take precedence
    if args and len(args) > 0:
        for idx, value in enumerate(args):
            if idx < len(attributes):
                setattr(self, attributes[idx], value)
    # Otherwise, we update based on kwargs
    else:
        for key, value in kwargs.items():
            if hasattr(self, key):  # Check if the object has the attribute
                setattr(self, key, value)
