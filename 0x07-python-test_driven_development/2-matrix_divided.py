#!/usr/bin/python3
"""
Maxtrix Division Module
Divides matrix
Yes
"""
def matrix_divided(matrix, div):
    """
        Matrix Divider
    """
    if len(matrix[0]) is not len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matric (list of lists) of integers/floats")
    if not isinstance(matrix[0], list) and not isinstance(matrix[1], list):
        raise TypeError("matrix must be a matric (list of lists) of integers/floats")
    
    for idx in matrix[0] + matrix[1]:
        if not isinstance(idx, int) and not isinstance(idx, float):
            raise TypeError("matix must be a matrix (list of lists) of integers/floats")
    
    matrix = (matrix[0], matrix[1])
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(count / div, 2) for count in idx]for idx in matrix]
