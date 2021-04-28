"""
https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
"""


def findThreeLargestNumbers(array):
    largest_nums = get_largest_nums(array)
    return create_sorted_array(largest_nums)


def get_largest_nums(array):
    if len(array) == 3:
        return create_sorted_array(array)

    largest_nums = []

    while len(largest_nums) < 3:
        largest_num = max(array)
        index_of_largest = array.index(largest_num)
        largest_nums.append(largest_num)
        array.pop(index_of_largest)
    return largest_nums


def find_smallest(array):
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < array[smallest_index]:
            smallest_index = i
    return smallest_index


def create_sorted_array(nums):

    new_array = []

    for i in range(len(nums)):
        index_smallest_num = find_smallest(nums)
        num_at_index = nums.pop(index_smallest_num)
        new_array.append(num_at_index)
    return new_array
