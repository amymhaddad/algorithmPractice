"""
https://leetcode.com/problems/palindrome-number/
"""

# def isPalindrome(x):
#     if x < 0:
#         return False
#
#     if x > 0 and x < 10:
#         return True
#
#     num_string = str(x)
#     p1 = 0
#     p2 = len(num_string) -1 
#     
#     while p2 - p1 >= 1:
#         if num_string[p1] != num_string[p2]:
#             return False
#         else:
#             p1 += 1
#             p2 -= 1
#     return True

# def isPalindrome(x):

#     if x < 0:
#         return False

#     if x > 0 and x < 10:
#         return True

#     original_num = x 
#     new_num = []

#     while original_num > 0:
#         new_num.append(original_num % 10)
#         original_num = original_num // 10

#     for num in new_num[::-1]:
#         if num != x % 10:
#             return False
#         x = x // 10

#     return True

