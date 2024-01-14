def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set = set()

    # Iterate through elements in set_1
    for element in set_1:
        # Check if the element is also in set_2
        if element in set_2:
            # Add the common element to the common_set
            common_set.add(element)

    return common_set
