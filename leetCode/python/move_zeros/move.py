#https://leetcode.com/problems/move-zeroes/

# def move_zeros(nums):
#     if len(nums) == 1:
#         return nums

#     i = 0

#     while i < len(nums) -1:
#         import pdb; pdb.set_trace()
#         if nums[i] == 0:
#             zero = nums.pop(nums[i])
#             nums.append(zero)
#         else:
#             i += 1
#     return nums

def move_zeros(nums):


print(move_zeros([0, 1, 0, 3, 12]))
