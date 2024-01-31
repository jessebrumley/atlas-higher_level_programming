#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a new rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of a new rectangle.
            height (int): the height of a new rectangle.
            x (int): the x location of new rectangle.
            y (int): the y location of new rectangle.
        Raises:
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
