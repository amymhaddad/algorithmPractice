"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
"""


def min_operations(nums):

    prev_num = nums[0]
    total_operations = 0

    for i, curr_num in enumerate(nums[1:]):
        if curr_num > prev_num:
            prev_num = curr_num
            continue
        curr_operations = (prev_num - curr_num) + 1
        total_operations += curr_operations
        prev_num = curr_num + curr_operations
    return total_operations
