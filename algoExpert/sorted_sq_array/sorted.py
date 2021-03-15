"""
https://www.algoexpert.io/questions/Sorted%20Squared%20Array
"""


def sq_array(array):
    return [num * num for num in array]


def smallest_index(array):
    smallest_index = 0
    smallest_value = array[0]

    for i in range(1, len(array)):
        current_value = array[i]
        if current_value < smallest_value:
            smallest_index = i
            smallest_value = current_value

    return smallest_index


def sorted_squared_array(array):
    squared_array = sq_array(array)
    sorted_array = []

    for i in range(len(squared_array)):
        next_smallest_index = smallest_index(squared_array)
        next_smallest_value = squared_array.pop(next_smallest_index)
        sorted_array.append(next_smallest_value)
    return sorted_array
