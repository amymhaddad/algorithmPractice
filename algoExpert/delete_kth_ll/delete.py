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
            break
       
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

update = removeKthNodeFromEnd(a, k)

while update is not None:
    print(update.value)
    update = update.next
  
