"""
https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
"""

nums = [-1, 0, 3, 5, 9, 12]
target = 9


def binary(nums, target):
    if not nums:
        return -1
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary(nums, target))
