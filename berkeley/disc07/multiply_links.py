"""
Write a function that takes in a Python list of linked lists and multiplies them element-wise. It should return a new linked list.

If not all of the Link objects are of equal length, return a linked list whose length is that of the shortest linked list given. You may assume the Link objects are shallow linked lists, and that lst_of_lnks contains at least one linked list.
"""
class Link:
   empty = ()
  
   def __init__(self, first, rest=empty):
       self.first = first
       self.rest = rest

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
   # valid = all(ele.rest is Link.empty for ele in lst_of_lnks)
    #import pdb; pdb.set_trace()
    for ele in lst_of_lnks:
        if ele == Link.empty:
            return 0

    total = 1
    for ele in lst_of_lnks:
        total *= ele.first 
    
    new_list = []   
    for ele in lst_of_lnks:
        new_list.append(ele.rest)
    return total + multiply_lnks(new_list)
        


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])


print(p)
