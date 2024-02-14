#!/usr/bin/python3
"""Square class that inherits from Rectangle class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of the Square class.

        Args:
            size (int): The width and height of the Square.
            x (int): The x coordinate of the Square.
            y (int): The y coordinate of the Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
