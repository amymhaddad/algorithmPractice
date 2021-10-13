#https://leetcode.com/problems/palindrome-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        while head.next is not None:
            values.append(head.val)
            head = head.next 

        p1 = 0
        p2 = len(values) -1

        while p2 - p1 > 1:
            if values[p2] != values[p1]:
                return False

            p1 += 1
            p2 += 1
        return True


    
