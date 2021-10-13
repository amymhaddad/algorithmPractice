#https://leetcode.com/problems/palindrome-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Solution 1
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        while head is not None:
            values.append(head.val)
            head = head.next 

        p1 = 0
        p2 = len(values) -1
        while p1 < p2:
            if values[p2] != values[p1]:
                return False

            p1 += 1
            p2 -= 1
        return True

#Solution 2
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        
        temp = head 
        
        while temp:
            values.append(temp.val)
            temp = temp.next
  
        while head:
            if values.pop() != head.val:
                return False
            head = head.next
        return True

#Solution 3
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
