"""
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
"""

def sq_root(num):
    low = 0
    high = num + 1

    while low < high:
        curr = (low + high) // 2

        if curr * curr == num or num in in_range(curr):
            return curr
        elif num > curr:
            high = curr - 1
        else:
            low = curr + 1
    return -1

def in_range(num):
    res = []

    lower = num * num 
    upper = (num + 1) * (num + 1)
    for i in range(lower, upper):
        res.append(i)
    return num in res

#print(lower, upper)

print(sq_root(4))



