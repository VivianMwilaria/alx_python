def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate through the elements of the current row and square each value
        for element in row:
            squared_value = element ** 2
            result_row.append(squared_value)

        # Append the squared row to the result matrix
        result_matrix.append(result_row)

    return result_matrix

