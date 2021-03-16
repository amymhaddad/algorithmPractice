"""
Write a procedure merge(n1, n2) which takes numbers with digits in decreasing order and returns a single number with all of the digits of the two, in decreasing order. Any number merged with 0 will be that number (treat 0 as having no digits). Use recursion.
"""

def merge(n1, n2):
    import pdb; pdb.set_trace()
    if n1 == 0:
        return n1
    elif n2 == 0:
        return n2

    else:
        n1_base = n1 // 10 * 10 
        n2_base = n2 // 10 * 10

        if n1_base < n2_base:
            return n1_base + merge(n1 // 10, n2)
        else:
            return merge(n1, n2 // 10)

print(merge(31, 42))
