"""
https://www.algoexpert.io/questions/Validate%20BST
"""
import math

class TreeNode:
   def __init__(self, value=0, left=None, right=None):
       self.value = value
       self.left = left
       self.right = right

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)


def validateBst(tree, high=math.inf, low=-math.inf):
    if tree.right is None and tree.left is None:
        return True 

    if tree.value < low or tree.value > high:
         return False
    #import pdb; pdb.set_trace()
    if tree.value <= high and tree.value > low:
        validateBst(tree.left, high=tree.value, low=low)

    if tree.value > low and tree.value <= high:
        validateBst(tree.right, high=high, low = tree.value)
print(validateBst(root))
