
class Link:
   empty = ()
  
   def __init__(self, first, rest=empty):
       self.first = first
       self.rest = rest



def sum_nums(link):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if link is Link.empty:
        return 0

    else:
        return link.first + sum_nums(link.rest)

a = Link(1, Link(6, Link(7)))


#compute the product of all the firsts in our list of Links.
#Then, the subproblem we use here is the rest of all the linked lists in our list of Links
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

    new_list = []
    total = 1
    for linked_list in lst_of_lnks:
        if linked_list is Link.empty:
            return total
        else:
            total *= linked_list.first 
            new_list.append(linked_list.rest)
    return Link(total, multiply_lnks(new_list))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])

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
    if link is Link.empty or link.rest is Link.empty:
        return 
    
    link.first, link.rest.first = link.rest.first, link.first
    flip_two(link.rest.rest)


lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))

def iterative_flip_two(link):
    while link is not Link.empty and link.rest is not Link.empty:
        link.first, link.rest.first = link.rest.first, link.first
        link = link.rest.rest

iterative_flip_two(lnk)

print(lnk.first, lnk.rest.first)