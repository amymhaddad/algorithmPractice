"""
https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
"""
from collections import deque


class Link:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    while k > 0:
        second = second.next
        k -= 1

    if second is None:
        first.value = first.next.value
        first.next = first.next.next
        return

    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next
