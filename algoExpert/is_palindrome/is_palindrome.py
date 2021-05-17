"""
https://www.algoexpert.io/questions/Palindrome%20Check
"""


def is_palendrome(string):
    if len(string) <= 1:
        return True

    return string[0] == string[-1] and is_palendrome(string[1:-1])


def v2_is_palendrome(string):
    p1 = 0
    p2 = len(string) - 1

    while p2 - p1 >= 1:
        if string[p1] != string[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True
