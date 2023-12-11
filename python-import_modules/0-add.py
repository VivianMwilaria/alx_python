# File: add_0.py
# Contains the function def add(a, b)

def add(a,b):
    a = 1
    b = 2
sum_result = add(a, b)
# Importing the add function from add_0.py
from add_0 import add


# Printing the result using string formatting
print("{} + {} = {}".format(a, b, add(a, b)))
