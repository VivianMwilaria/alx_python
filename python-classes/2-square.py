"""
Module 1-square
Define class Square with private attribute size
"""

class Square:
    """"class is square"""
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size: size of a square
        """
        self.__size = size
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return self.__size ** 2
