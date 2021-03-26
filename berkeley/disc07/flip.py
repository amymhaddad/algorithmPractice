"""
Write a recursive function flip_two that takes as input a linked list s and mutates s so that every pair is flipped.
"""

class Link:
   empty = ()
  
   def __init__(self, first, rest=empty):
       self.first = first
       self.rest = rest

def flip_two_iterative(link):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """

    while link is not Link.empty and link.rest is not Link.empty:
        link.first, link.rest.first = link.rest.first, link.first 
        link = link.rest.rest 


#Recur sol:
def flip_two(link):
    if link is Link.empty or link.rest is Link.empty:
        return 
    
    link.first, link.rest.first = link.rest.first, link.first 

    flip_two(link.rest.rest)

lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
flip_two(lnk)

while lnk is not Link.empty:
    print(lnk.first)
    lnk = lnk.rest 