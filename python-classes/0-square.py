class Square:
    """
    Represents a square with a size attribute.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def get_size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, size):
        """
        Sets the size of the square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
