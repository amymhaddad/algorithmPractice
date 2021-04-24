"""
https://www.algoexpert.io/questions/Binary%20Search
"""

def binary(array, target):

    low = 0
    high = len(array) 

    while high - low > 1:
        mid = (high + low) // 2
        if array[mid] >= target:
            high = mid
        
        else:
            low = mid 
    #import pdb; pdb.set_trace() 
    if mid == high:
        return low
    elif array[mid] == target:
        return mid

    elif target > high or target < low:
        return -1
#arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
#target = 0

arr = [1, 2, 2, 3, 4]
target = 2
print(binary(arr, target))
