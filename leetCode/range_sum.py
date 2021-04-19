"""
https://leetcode.com/problems/range-sum-of-bst/
"""

def rangeSumsBST(root, low, high):
    return helper(root, low, high, 0)

def is_in_range(current_value, low, high):
    return any(i == current_value for i in range(low, high+1))

def helper(root, low, high, running_total):
    if root is None:
        return 
    
    if is_in_range(root.value, low, high):
        running_total += root.value

    if root.right is None and root.left is None:
        return running_total
    if root.left:
        return helper(root.left, low, high, running_total)
    if root.right:
        return helper(root.right, low, high, running_total)
