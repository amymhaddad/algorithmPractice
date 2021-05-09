"""
https://www.algoexpert.io/questions/Bubble%20Sort
"""

array = [8, 9, 3]
def smallest_index(array):
    smallest_index = 0 
    for i, num in enumerate(array[1:], 1):
        if array[i] < array[smallest_index]:
            smallest_index = i
    return smallest_index

def sort_array(array):
    new_arr = []
    for i in range(len(array)):
        index = smallest_index(array)
        next_num = array.pop(index)
        new_arr.append(next_num)
    return new_arr

#print(sort_array(array))

def bubbleSort(array):
    array_length = len(array)

    while array_length >= 0:
        swap = 0 
        next_num = 1 
        first_num = 0
        while next_num <= len(array) -1: 
            if array[first_num] > array[next_num]:
                swap += 1
                array[first_num], array[next_num] = array[next_num], array[first_num]
            next_num += 1
            first_num += 1
        if swap == 0:
            return array
        array_length -= 1
    return array

print(bubbleSort(array))

