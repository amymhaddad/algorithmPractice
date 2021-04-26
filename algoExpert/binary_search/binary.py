"""
https://www.algoexpert.io/questions/Binary%20Search
"""


def binary(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
