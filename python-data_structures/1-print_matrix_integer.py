def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for element in row:
            # Use str.format() to print integers without casting to strings
            print("{:d}".format(element), end=" ")
    print()  # Move to the next line after printing each row
