"""
https://www.algoexpert.io/questions/Bubble%20Sort
"""

array = [8, 5, 2, 9, 5, 6, 3]
def smallest_index(array):
    smallest_index_so_far = 0 
 
    for i in range(len(array[1:])):
        curr_val = array[i]
        prev_val = array[smallest_index_so_far]
        if curr_val < prev_val:
            smallest_index_so_far = i
    return smallest_index_so_far

def sort_array(array):
    new_arr = []
    for i in range(len(array)):
        index = smallest_index(array)
        next_num = array.pop(index)
        new_arr.append(next_num)
    return new_arr

print(sort_array(array))
