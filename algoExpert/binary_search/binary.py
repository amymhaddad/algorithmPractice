"""
https://www.algoexpert.io/questions/Binary%20Search
"""

# Sol 1 - use while loop
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


# Sol 2 - use recursion w/helper function
def binarySearch(array, target):
    def find_target(current_array):
        if not current_array:
            return -1

        mid = len(current_array) // 2

        if current_array[mid] == target:
            return current_array[mid]

        if target < current_array[mid]:
            return find_target(current_array[:mid])
        else:
            return find_target(current_array[mid + 1 :])

    current_array = array
    item = find_target(current_array)
    if item > 0:
        return array.index(item)
    return item


# Sol 3 - recursion w/2 functions
def v3_binarySearch(array, target):
    item = find_target(array, target)
    if item > 0:
        return array.index(item)
    return item


def find_target(current_array, target):
    if not current_array:
        return -1

    mid = len(current_array) // 2

    if current_array[mid] == target:
        return current_array[mid]

    if target < current_array[mid]:
        return find_target(current_array[:mid], target)
    else:
        return find_target(current_array[mid + 1 :], target)
