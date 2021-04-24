"""
https://www.algoexpert.io/questions/Binary%20Search
"""

def binary(array, target):

    low = 0
    high = len(array) 

    while high - low > 1:
        mid = (high + low) // 2

        #import pdb; pdb.set_trace()
        if array[mid] >= array[low]:
            high = mid
        else:
            low = mid 

    import pdb; pdb.set_trace()
    if array[high] == target:
        return mid
    else:
        return -1
    #import pdb; pdb.set_trace()
#     if array[mid] == target:
#         return mid
#     else:
#         return -1
# # arr = [1, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33
arr = [1, 2, 2, 3, 4]
target = 2

print(binary(arr, target))
