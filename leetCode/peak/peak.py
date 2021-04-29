"""
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
"""


def peak(arr):
    max_so_far = arr[0]

    for i, num in enumerate(arr[1:]):
        if num > max_so_far:
            max_so_far = num

    return arr.index(max_so_far)
