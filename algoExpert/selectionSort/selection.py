"""
https://www.algoexpert.io/questions/Selection%20Sort
"""

# Version 1
def selection(arr):
    sm_index = 0

    while sm_index < len(arr) - 1:
        curr_pointer = sm_index
        for i, next_num in enumerate(arr[sm_index + 1 :], sm_index + 1):
            if next_num < arr[curr_pointer]:
                curr_pointer = i
        arr[sm_index], arr[curr_pointer] = arr[curr_pointer], arr[sm_index]
        sm_index += 1
    return arr


# Version 2
def selectionSort(arr):
    curr_index = 0

    while curr_index < len(arr) - 1:

        sm_index = curr_index

        for i in range(curr_index + 1, len(arr)):
            if arr[i] < arr[sm_index]:
                sm_index = i
        swap(curr_index, sm_index, arr)
        curr_index += 1
    return arr


def swap(curr_index, sm_index, arr):
    arr[curr_index], arr[sm_index] = arr[sm_index], arr[curr_index]
