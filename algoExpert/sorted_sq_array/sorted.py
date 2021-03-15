"""
https://www.algoexpert.io/questions/Sorted%20Squared%20Array
"""

array = [1, 2, 3, 5, 6, 8, 9]

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

print(smallest_index(array))
