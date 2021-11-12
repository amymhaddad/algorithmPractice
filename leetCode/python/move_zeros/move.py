# #https://leetcode.com/problems/move-zeroes/
#
# def move_zeros(nums):
#     nums.sort()
#     first_num_index = 1
#     for i, num in enumerate(nums):
#         if num > 0:
#             first_num_index = i
#             break
#     return nums[first_num_index:] + nums[:first_num_index]


def move_zeros(nums):
    p1 = 0
    p2 = 1

    for num in nums:
        if p2 >= len(nums):
            break 
        if nums[p1] == 0 and nums[p2] > 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
        elif nums[p1] == 0 and nums[p2] == 0:
            p2 += 1
    return nums

print(move_zeros([1,0,1]))
