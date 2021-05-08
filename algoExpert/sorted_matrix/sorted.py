"""
https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix
"""


def searchInSortedMatrix(matrix, target):
    """
    Determine if a given target is in a row within the given matrix.
    If a target is in a row, then return the row, index and target.
    Otherwise return [-1, -1] because the target value doesn't exist in any row.
    """
    row_index = None
    for i, row in enumerate(matrix):
        if target in row:
            row_index = i
            return find_target(row, row_index, target)
    return [-1, -1]


def find_target(row, row_index, target):
    """
    Find the target in a given row and return the indices for where it's found in a matrix.
    """
    low = 0
    high = len(row) - 1

    while low <= high:
        col_index = (low + high) // 2
        if row[col_index] == target:
            return [row_index, col_index]
        elif row[col_index] < target:
            low = col_index + 1
        else:
            high = col_index - 1

    return [-1, -1]
