class Square:
    """class that defines square"""

    """The __init__ method is run as soon as the object is instatiated
    Args : 
    Size: The sixe of the square. I must be a positive integer.
    Attribute: 
    __size: rivaye instance attribute that is the size of the square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

