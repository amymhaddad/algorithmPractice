"""
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1003/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Iterative solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        if current is None:
            return TreeNode(val)
        
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
        return root