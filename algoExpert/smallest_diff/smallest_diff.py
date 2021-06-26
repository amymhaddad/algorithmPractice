"""
https://www.algoexpert.io/questions/Smallest%20Difference
"""


def smallest(arr1, arr2):
    arr1.sort()
    arr2.sort()
    index_1 = 0
    index_2 = 0
    smallest_diff = float("inf")
    current_diff = float("inf")
    pairs = []

    while index_1 < len(arr1) and index_2 < len(arr2):
        first_num = arr1[index_1]
        second_num = arr2[index_2]

        if first_num < second_num:
            current_diff = second_num - first_num
            index_1 += 1

        elif first_num > second_num:
            current_diff = first_num - second_num
            index_2 += 1
        else:
            return [first_num, second_num]

        if smallest_diff > current_diff:
            smallest_diff = current_diff
            pairs = [first_num, second_num]
    return pairs
