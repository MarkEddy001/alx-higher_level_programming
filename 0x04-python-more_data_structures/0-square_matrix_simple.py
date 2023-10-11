#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

  Args:
    matrix: A 2-dimensional array.

  Returns:
    A new matrix of the same size as `matrix`, with each value squared.
    """
    new_matrix = []

    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return new_matrix
