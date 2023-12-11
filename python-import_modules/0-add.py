# File: add_0.py
# Contains the function def add(a, b)

# File: main_program.py
a = 1
b = 2

# Importing the add function from add_0.py
from add_0 import add

# Printing the result using string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
