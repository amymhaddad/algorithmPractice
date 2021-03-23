"""
Write a function that takes in a a linked list and returns the sum of all its elements. You may assume all elements in s are integers.
"""

class Link:
   empty = ()
  
   def __init__(self, first, rest=empty):
       self.first = first
       self.rest = rest

def sum_nums(nums):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if nums == Link.empty:
        return 0

    else:
        return nums.first + sum_nums(nums.rest)

a = Link(1, Link(6, Link(7)))
print(sum_nums(a))
