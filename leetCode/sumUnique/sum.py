"""

https://leetcode.com/problems/sum-of-unique-elements/
"""
from collections import Counter

array = [1, 2, 3, 2]

# Solution 1
def sum_ele(array):
    counter = {}

    for num in array:
        counter[num] = counter.get(num, 0) + 1

    sum_unique = 0
    for num, count in counter.items():
        if count == 1:
            sum_unique += num
    return sum_unique


# Sol 2
def sum_ele_v2(array):
    counter = Counter(array)

    total = 0
    for num, count in counter.items():
        if count == 1:
            total += num

    return total


def sum_ele_v3(array):
    return sum(num for num, count in Counter(array).items() if count == 1)
