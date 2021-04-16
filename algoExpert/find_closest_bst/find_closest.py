"""
https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
"""
import math 
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
 
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

def findClosestValueInBst(tree, target):
    total_values = []
    get_tree_values(tree, total_values)
    return total_values


def get_tree_values(tree, total_values):
    if tree is None:
        return 

    stack = [(tree, -math.inf, math.inf)]
    
    while stack:
        node, lower, upper = stack.pop()

        if node is None:
            continue

        val = node.val
        if val >= upper or val <= lower:
            continue
        total_values.append(val)
        stack.append((node.left, lower, val))
        stack.append((node.right, val, upper))
    return total_values

print(findClosestValueInBst(root, 2))


