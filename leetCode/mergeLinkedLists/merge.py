"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        elif l1.val <= l2.val:
            return ListNode(l1.val, self.mergeTwoLists(l2, l1.next))
        else:
            return ListNode(l2.val, self.mergeTwoLists(l1, l2.next))
