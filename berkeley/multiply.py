"""
Write a function that takes two numbers m and n and returns their product. Assume m and n are positive integers. Use recursion, not mul or *!
"""

def multiply(n1, n2):
    if n2 <= 1:
        return n1
    else:
        return n1 + multiply(n1, n2 -1)

#print(multiply(6, 3))

def tail_multiply(n1, n2):


    def helper(n1, n2):
        if n2 == 1:
            #import pdb; pdb.set_trace()
            return 1  

        else:
            print(n1)
            return helper(n1+ n1-1, n2-1)
    return helper(n1, n2)

print(tail_multiply(5, 3))




