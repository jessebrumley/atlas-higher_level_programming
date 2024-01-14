#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if item != len(matrix[row]):
                stop = ' '
            else:
                stop = ''
        print("[:d]".format(matrix[row][col]), end=stop)
    print()
