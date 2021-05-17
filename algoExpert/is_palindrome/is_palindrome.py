"""
https://www.algoexpert.io/questions/Palindrome%20Check
"""

def is_palendrome(string):
    if len(string) == 1:
        return True

    return string[0] == string[-1] and is_palendrome(string[1:-1])

string = "abaa"
print(is_palendrome(string))
