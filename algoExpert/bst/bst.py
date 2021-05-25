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


def validateBst(tree, low=-math.inf, high=math.inf):
    if tree is None:
        return True

    if tree.value < low or tree.value >= high:
        return False

    return validateBst(tree.left, low, tree.value) and validateBst(
        tree.right, tree.value, high
    )
