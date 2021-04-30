"""
https://www.algoexpert.io/questions/Minimum%20Waiting%20Time
"""


def min_waiting_time(array):
    array.sort()

    prev = 0
    curr = array[0]
    total = []

    for num in array[1:]:
        total.append(prev + curr)
        prev += curr
        curr = num
    return sum(total)
