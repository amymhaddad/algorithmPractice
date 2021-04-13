"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
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

def level_order(root):
    if root is None:
        return 
    if root == []:
        return []

    que = deque()
    que.append([0, root])

    level = 0
    total_nodes = []
    nodes_per_level = []

    while que:
        node_info = que.pop()
        node_level, val = node_info[0], node_info[1]
        
        if val is None:
            continue

        if node_level > level:
            level = node_level
            total_nodes.append(nodes_per_level)
            nodes_per_level = []
        nodes_per_level.append(val.val) 
        
    
        que.appendleft([level+1, val.left])
        que.appendleft([level+1, val.right])
    return total_nodes

print(level_order(root))
