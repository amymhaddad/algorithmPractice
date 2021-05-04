"""
https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
"""
from collections import deque

class Link:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    current = head
    que = deque()
    
    while current is not None:
        que.appendleft(current.value)
        current = current.next

    val_to_remove = que.index(k - 1)

    while head is not None:
       # import pdb; pdb.set_trace()
        if head.next is None:
            head = head.next
#            break
       
        elif head.next.value == val_to_remove:
            head = head.next.next
        else:
            head = head.next 

a = Link(1)
b = Link(2)
c = Link(3)
d = Link(4)
a.next = b
b.next = c
c.next = d 


k = 2


def remove(head, k):
    first = head
    second = head
    counter = 1 

    while counter <= k:
        second = second.next
        counter += 1
   
    prev = first
    while second is not None:
        if second.next is None:
            prev.next = second
            break
        second = second.next
        first = first.next
        prev = first
    return prev
  
#update = remove(a, k)

def v2_remove(head, k):
    first = head
    second = head
    counter = 1 

    #want to be inclusive -- move k spots so second is k spots ahead of first
    while counter <= k:
        second = second.next
        counter += 1

    #check if second is already at None
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    
    #Set this condition w/second.next so second.value points to the last 
    #value in the LL -- not to None. This means that first points to the value
    #right before the one I need to delete
    while second.next is not None:
        second = second.next
        first = first.next 
    
    import pdb; pdb.set_trace()

print(v2_remove(a, 2))

   
 
