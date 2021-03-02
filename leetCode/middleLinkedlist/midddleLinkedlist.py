class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        all_nums = []
        
        current_node = head 
       
        while current_node is not None:
            all_nums.append(current_node.val)
            current_node = current_node.next 
            
        index = len(all_nums) // 2
        current_node = head   
        while index >= 0:
            if index == 0:
                return current_node
            else:
                index -= 1
                current_node = current_node.next
