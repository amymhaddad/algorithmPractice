"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
"""

from stack import Stack


class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(3)
root.right = Tree(4)

# First sol
def in_order(root):
    if root is None:
        return

    if root == []:
        return []

    stack = Stack()
    results = []

    while True:
        if root is not None:
            stack.push(root)
            root = root.left

        else:
            if stack.is_empty():
                break
            root = stack.pop()
            results.append(root.val)
            root = root.right
    return results


# 2nd sol w/double while loop
def in_order(root):
    if root is None:
        return

    if root == []:
        return []

    stack = Stack()
    results = []

    while True:
        while root is not None:
            stack.push(root)
            root = root.left

        if stack.is_empty():
            break
        root = stack.pop()
        results.append(root.val)
        root = root.right
    return results
