"""
https://leetcode.com/problems/palindrome-number/
"""

def isPalindrome(x):
    if x < 10:
        return True

    num_string = str(x)
    p1 = 0
    p2 = len(num_string) -1 

    while p2 - p1 >= 1:
        if num_string[p1] != num_string[p2]:
            return False
        else:
            p1 += 1
            p2 -= 1
    return True

