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
        current = current.value

    val_to_remove = que.index(k - 1)

    while head is not None:
        if head.next.val == val_to_remove:
            head = head.next.next
        else:
            head = head.next 

a = Link(2, Link(3, Link(5)))
k = 1

#print(removeKthNodeFromEnd(a, k))
print(a)    
