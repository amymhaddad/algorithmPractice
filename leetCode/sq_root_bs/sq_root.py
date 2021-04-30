"""
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
"""


def sq_root(num):
    if num <= 1:
        return num
    low = 1
    high = num

    while high - low > 1:
        mid = (low + high) // 2

        if mid * mid >= num:
            high = mid
        else:
            low = mid

    if high * high == num:
        return high
    return low
