#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size."""
        return self.width  # Because in a square, width is equal to height.

    @size.setter
    def size(self, value):
        """Setter for size, ensuring it sets both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attributes = ["id", "size", "x", "y"]

        if args and len(args) > 0:
            for idx, value in enumerate(args):
                if idx < len(attributes):
                    setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    
    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.
        """
        return {
            'id': self.id,
            'size': self.width,  # width and height are the same for a Square
            'x': self.x,
            'y': self.y
        }
    
    
    



