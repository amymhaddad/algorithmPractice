"""
Determine if a string is a palindrome
"""

# Sol 1: recursion
# O(n)
string = "abba"


def isPalindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])


# Sol 2: pointers
# O(n) | O(1)
def isPalindrome_v2(string):
    p1 = 0
    p2 = len(string) - 1

    while p1 < p2:
        if string[p1] != string[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True
