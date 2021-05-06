"""
https://www.algoexpert.io/questions/Tandem%20Bicycle
"""


def calculate_speed(red, blue):
    total = 0
    for i in range(len(red)):
        max_speed = max(red[i], blue[i])
        total += max_speed
    return total


def find_max_speeds(red, blue):
    red.sort(reverse=True)
    blue.sort()
    return calculate_speed(red, blue)


def find_min_speeds(red, blue):
    red.sort()
    blue.sort()
    return calculate_speed(red, blue)


def tandem(red, blue, fastest):
    if fastest:
        return find_max_speeds(red, blue)
    return find_min_speeds(red, blue)
