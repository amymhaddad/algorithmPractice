"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
"""
from stack import Stack 

class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.right.left = Tree(4)
root.right.right = Tree(5)

def pre(root):
    if root is None:
        return 

    if root == []:
        return []

    stack = Stack()
    stack.push(root)
    results = []

    while not stack.is_empty():
        curr_root = stack.pop()
        results.append(curr_root.val)

        if curr_root.right is not None:
            stack.push(curr_root.right)

        if curr_root.left is not None:
            stack.push(curr_root.left)

    return results

print(pre(root))
