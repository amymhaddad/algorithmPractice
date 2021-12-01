"""
https://leetcode.com/problems/palindrome-number/
"""
import collections

#Solution 1
def isPalindrome(x):
    if x < 0 :
        return False
    
    d1 = collections.deque()
    d2 = collections.deque()
    while x > 0:
        d1.appendleft(x%10)
        d2.append(x%10)
        x = x // 10
    return d1 == d2

#Solution 2
def isPalindrome(x):
    digits = list(str(x))
    deq = collections.deque(digits)

    while len(deq) > 1:
        if digits.pop() != deq.popleft():
            return False
    return True

#Solution 3
def isPalindrome(x):
    if x < 0:
        return False

    if x > 0 and x < 10:
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

#Solution 4
def isPalindrome(x):

    if x < 0:
        return False

    if x > 0 and x < 10:
        return True

    original_num = x 
    new_num = []

    while original_num > 0:
        new_num.append(original_num % 10)
        original_num = original_num // 10

    for num in new_num[::-1]:
        if num != x % 10:
            return False
        x = x // 10

    return True
    