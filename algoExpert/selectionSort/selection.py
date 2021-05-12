"""
https://www.algoexpert.io/questions/Selection%20Sort
"""

def smallest_index(array):
    smallest = 0 

    for i in range(len(array[1:])):
        if array[i] < array[smallest]:
            smallest = i
    return smallest



def selection(arr):
    j = 0

    while j < len(arr):

        for i, num in enumerate(range(len(arr)), 1):
            print(i)
            if arr[i] < arr[j]:
                continue
            elif arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
                break

    return arr
print(selection([4, 2, 5, 1]))
