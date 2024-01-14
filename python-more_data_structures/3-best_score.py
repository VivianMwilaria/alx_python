def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Initialize variables to store the best key and the maximum value
    best_key = None
    max_value = float('-inf')  # Initialize to negative infinity

    # Iterate through the dictionary items
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the maximum value
        if value > max_value:
            max_value = value
            best_key = key

    return best_key

