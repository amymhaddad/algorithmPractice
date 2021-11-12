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
    nums.sort()

    p1 = 0
    p2 = 1

    while p2 < len(nums):

        while nums[p2] > 0:
            p2 += 1
        nums[p1], nums[p2] = nums[p2], nums[p1]
        p1 += 1
        p2 += 1

    return nums


