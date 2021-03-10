class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        reversed = ListNode(head.val)

        while head.next is not None:

            next_val = head.next.val
            reversed.val, reversed.next = head.next.val, ListNode(
                reversed.val, reversed.next
            )

            head = head.next
        return reversed
