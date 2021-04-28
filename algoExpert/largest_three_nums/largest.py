"""
https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
"""

def find_largest_three_nums(array):
    if len(array) == 3:
        return array
    
    largest_nums = []

    while len(largest_nums) < 3:
        largest = max(array)
        index_of_largest = array.index(largest)
        largest_nums.append(largest)
        array.pop(index_of_largest)
    return largest_nums


array = [10, 5, 9, 10, 12]
print(find_largest_three_nums(array))


