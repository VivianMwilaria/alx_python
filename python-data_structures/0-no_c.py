def no_c(my_string):
    # Initialize an empty string to store the result
    new_string = ""

    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char.lower() != 'c':
            # Append the character to the new string
            new_string += char

    return new_string
