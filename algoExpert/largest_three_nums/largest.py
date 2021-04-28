"""
https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
"""

def findThreeLargestNumbers(array):
    largest = get_largest_nums(array)
    return create_sorted_array(largest)

def get_largest_nums(array):
    
    if len(array) == 3:
        return create_sorted_array(array)
    
    largest_nums = []

    while len(largest_nums) < 3:
        largest = max(array)
        index_of_largest = array.index(largest)
        largest_nums.append(largest)
        array.pop(index_of_largest)
    return largest_nums


def find_smallest(array):
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < array[smallest_index]:
            smallest_index = i 
    return smallest_index 


#update var names
def create_sorted_array(largest):

    new_array = []

    for i in range(len(largest)):
        index = find_smallest(largest)
        num = largest.pop(index)
        new_array.append(num)
    return new_array

array = [10, 5, 9, 10, 12]
print(findThreeLargestNumbers(array))