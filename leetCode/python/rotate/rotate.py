
def rotate(nums, k):

    while k > 0:
        last_num = nums.pop(-1)
        nums.insert(0, last_num)
        k -= 1
    return nums

