
#Solution 1
def rotate(nums, k):

    while k > 0:
        last_num = nums.pop(-1)
        nums.insert(0, last_num)
        k -= 1
    return nums

#Solution 2
def rotate(nums, k):
    nums_len = len(nums)
    rotated_array = [None] * nums_len

    for i, num in enumerate(nums):
        rotated_index = (k + i) % nums_len
        rotated_array[rotated_index] = num
    
    for i in range(nums_len):
        nums[i] = rotated_array[i]
