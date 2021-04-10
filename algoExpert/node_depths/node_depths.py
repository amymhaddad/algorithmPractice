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

# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)


def bfs(root):
    if root is None:
        return 
    que = deque()
    que.append(root)
    
    total = []
    head = root 
    level = 0
    while True:   
        root = que.pop()
        if root == head:
            total.append(0)

        if not que:
            level += 1
       
        if root.left is None and root.right is None:
            
            return sum(total)
        
        else:
            #level += 1
            if root.left: 
                que.appendleft(root.left)
                total.append(level)
            if root.right:
                que.appendleft(root.right)
                total.append(level)

   # return total 
print(bfs(root))
#Need to move the level -- this should only increment when the que is empty

