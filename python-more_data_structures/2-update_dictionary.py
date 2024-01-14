def update_dictionary(a_dictionary, key, value):
    # Update the value if the key exists, or add a new key-value pair if it doesn't
    a_dictionary[key] = value
    return a_dictionary

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Updating existing key 'b'
update_dictionary(my_dict, 'b', 10)
print(my_dict)  # Output: {'a': 1, 'b': 10, 'c': 3}

# Adding a new key 'd'
update_dictionary(my_dict, 'd', 4)
print(my_dict)  # Output: {'a': 1, 'b': 10, 'c': 3, 'd': 4}
