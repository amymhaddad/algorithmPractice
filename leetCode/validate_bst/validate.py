"""
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
#root.left.left = TreeNode(3)

def in_order(root):
    stack = []
    res = []

    while True:
             
        if root:
            #import pdb; pdb.set_trace()
            left_node_is_valid = root.left is None or root.val >= root.left.val
            right_node_is_valid = root.right is None or root.val <= root.right.val
            if left_node_is_valid and right_node_is_valid:
                stack.append(root)
                root = root.left 
            else:
                return False

        else:
            if len(stack) == 0:
                break 
            root = stack.pop()
            root = root.right
    return True

print(in_order(root))

