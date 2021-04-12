"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


def maxDepth(root):
    if root is None or root == []:
        return 0
    q1 = deque()
    q1.append([1, root])
    q2 = deque([])

    depth = 1
    while q1:
        node = q1.pop()
        depth, val = node[0], node[1]
        q2.appendleft([depth])
        if val.left is not None:
            q1.appendleft([depth + 1, val.left])
        if val.right is not None:
            q1.appendleft([depth + 1, val.right])
    return q2.popleft()[0]
