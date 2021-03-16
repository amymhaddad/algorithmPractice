"""
Write a procedure merge(n1, n2) which takes numbers with digits in decreasing order and returns a single number with all of the digits of the two, in decreasing order. Any number merged with 0 will be that number (treat 0 as having no digits). Use recursion.
"""

def merge(n1, n2):
    if n1 == 0:
        return n1
    elif n2 == 0:
        return n2

    elif n1 > n2:
        return (n1 // 10 * 10) + merge(n2, n1 % 10)
    else:
        return (n2 // 10 * 10) + merge(n1, n2 % 10)
print(merge(31, 42))

def merge_2(n1, n2):
     if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
