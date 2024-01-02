def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for index, element in enumerate(row):
            # Use str.format() to print integers without casting to strings
            if index == len(row) - 1:
                # If it's the last element in the row, print without trailing space
                print("{:d}".format(element))
            else:
                # Print the element with a trailing space
                print("{:d}".format(element), end=" ")

