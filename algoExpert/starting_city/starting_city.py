"""
https://www.algoexpert.io/questions/Valid%20Starting%20City
"""

arr = [1,2,3,4,5,6,7] 
k = 3
def rotate_array(arr, k):
    arr_length = len(arr)
    nums = len(arr) * [None]

    for i, value in enumerate(arr):
        import pdb; pdb.set_trace()
        index = (i + k) % arr_length
        nums[index] = value
    return nums
    
def rotate_index(arr, step, curr_index):
    indices = [i for i in range(len(arr))]
    print(indices)
    arr_length = len(arr)
    new_indices = arr_length * [None]

distances = [5, 25, 15, 10, 15]
step = 1
curr_index = 0
print(rotate_index(distances, step, curr_index))
