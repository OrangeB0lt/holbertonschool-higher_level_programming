#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda hori: list(map(lambda num: num * num), hori)), matrix)
