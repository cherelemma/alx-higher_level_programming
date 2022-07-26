#!/usr/bin/python3

"""Defines a class Rectangle"""

class Rectangle:
    """Represents a rectangle. No body."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ return width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle 
    
        Args:
            value (int): must be a +ve integer
        Raises:
            TypeError exception: If value is not an integer.
            ValueError exception: if value is less than zero
        """
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle 

        Args:
            value (int): must be a +ve integer
        Raises:
            TypeError exception: If value is not an integer.
            ValueError exception: if value is less than zero
        """
        if not isinstance (value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self): 
        """ that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self): 
        """that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(self.print_symbol) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """Return a string representation of the rectangle 
            to be able to recreate a new instance by using eval().
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (eval(rect))

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2): 
        """Returns the biggest rectangle based on the area.
        
        Args:
            reac_1 (Rectangle): The 1st instance of a rectangle
            rect_2 (Rectangle): The 2nd instance of a rectangle
        Raise:
            TypeError exception: if either of the instnce (reac_1 and rect_2) not an instance of a rectangle
        """ 
        if not isinstance (rect_1, Rectangle): 
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle): 
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2 

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))