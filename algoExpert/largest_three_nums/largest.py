"""
https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
"""

def find_largest_three_nums(array):
    if len(array) == 3:
        return sort_array(array)
    
    largest_nums = []

    while len(largest_nums) < 3:
        largest = max(array)
        index_of_largest = array.index(largest)
        largest_nums.append(largest)
        array.pop(index_of_largest)
    return sort_array(largest_nums)



array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
#print(find_largest_three_nums(array))

def sort_arr(array):
    max_index_so_far = 0

    for i in range(len(array[1:])):
        if array[i] < array[max_index_so_far]:
            max_index_so_far = i 

    return max_index_so_far

print(sort_arr([141, 18, 541]))


