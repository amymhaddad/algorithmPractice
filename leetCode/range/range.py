"""
https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
"""


def num_range(nums, target):
    start = -1
    end = -1

    for i, num in enumerate(nums):
        if num == target:
            if start < 0:
                start = i
            end = i 

    return [start, end]

nums = [5, 7, 7, 8, 8, 10]
target = 1

print(num_range(nums, target))


def range(nums, target):
    low = 1
    high = len(nums) - 1

    start, end = -1, -1

    while low-1 < high -1:
        mid = (low + high) // 2
        while nums[mid] == target:
            if nums[mid] < nums[mid-1]:
                start = mid 
                low += 1
                high += 1
            elif nums[mid] == nums[mid+1] and nums[mid] == nums[mid-1]:
                low += 1
                high += 1
            elif nums[mid] < nums[mid-1]:
                end = mid
    #Add code to account for searches that are too high /low 
    