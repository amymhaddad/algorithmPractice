"""
Write a recursive function flip_two that takes as input a linked list s and mutates s so that every pair is flipped.
"""

class Link:
   empty = ()
  
   def __init__(self, first, rest=empty):
       self.first = first
       self.rest = rest

def flip_two(link):
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
    head_node = link 

    while head_node.first is not Link.empty and head_node.rest is not Link.empty:
        head_node.first, head_node.rest.first = head_node.rest.first, head_node.first 

        head_node = head_node.rest.rest 

    return link

lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
vals = flip_two(lnk)

while vals is not Link.empty:
    print(vals.first)
    vals = vals.rest 

"""
-Need to check if first val is empty AND if rest is empty
-Swap the elements
-Update the head to SKIP the next value
-Return the given link (which has been mutated)


"""

#recur:
def flip_two_recur(link):
    head_node = link 
   # import pdb; pdb.set_trace()

    if link.first is Link.empty or link.rest is Link.empty:
        return 


    head_node.first, head_node.rest.first = head_node.rest.first, head_node.first 

    flip_two(head_node.rest.rest)

  

# lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
# vals = flip_two(lnk)


