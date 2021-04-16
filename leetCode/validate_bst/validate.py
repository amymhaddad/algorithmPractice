"""
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/
"""
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(1)

# Sol 1: recursion
def validate(root):
    def is_valid(node, lower=-math.inf, upper=math.inf):
        if node is None:
            return True
        if node.val >= upper or node.val <= lower:
            return False
        return is_valid(node.left, lower, node.val) and is_valid(
            node.right, node.val, upper
        )

    return is_valid(root)


# Sol 2: iteration
def iterative_validation(root):
    stack = [(root, -math.inf, math.inf)]

    while stack:
        node, lower, upper = stack.pop()
        if node is None:
            continue
        val = node.val

        if val >= upper or val <= lower:
            return False

        stack.append((node.left, lower, val))
        stack.append((node.right, val, upper))
    return True
