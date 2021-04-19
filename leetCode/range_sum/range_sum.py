"""
https://leetcode.com/problems/range-sum-of-bst/
"""
class Tree():
   def __init__(self, value, left = None, right = None):
       self.value = value
       self.left = left
       self.right = right

root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(3)
root.right = Tree(4)



def rangeSumsBST(root, low, high):
    return helper(root, low, high, 0)

def is_in_range(current_value, low, high):
    return any(i == current_value for i in range(low, high+1))

def helper(root, low, high, running_total):
    if root is None:
        return 
    #import pdb; pdb.set_trace() 
    if is_in_range(root.value, low, high):
        running_total += root.value

    if root.right is None and root.left is None:
        if is_in_range(root.value, low, high):
            running_total += root.value

    if root.left:
        return helper(root.left, low, high, running_total)

    if root.right:
        return helper(root.right, low, high, running_total)
print(rangeSumsBST(root, 1, 4))
