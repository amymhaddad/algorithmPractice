"""
https://www.algoexpert.io/questions/Node%20Depths
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)


# Time complexity - O(n) // Space - O(h)
# Sol 1
def nodeDepths(root):
    stack = [{"node": root, "depth": 0}]
    depth_count = 0

    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        depth_count += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return depth_count


# Sol 2
def nodeDepths(root):
    if root is None:
        return

    que = deque()
    que.append([0, root])
    total = []
    while que:
        node = que.pop()
        level, root = node[0], node[1]
        total.append(level)

        if root.left is not None:
            que.append([level + 1, root.left])
        if root.right is not None:
            que.append([level + 1, root.right])
    return sum(total)


# Sol 3
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    else:
        return (
            depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
        )
