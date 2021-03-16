"""
Write a function that takes two numbers m and n and returns their product. Assume m and n are positive integers. Use recursion, not mul or *!
"""
#Solution 1 
def multiply(n1, n2):
    if n2 <= 1:
        return n1
    else:
        return n1 + multiply(n1, n2 -1)

#Solution 2
def tail_multiply(n1, n2):

    def helper(n1, n2, result):
        if n2 == 0:
            return result
        else:
            return helper(n1, n2 -1, result + n1)
    return helper(n1, n2, 0)

    return helper
print(tail_multiply(5, 3))
