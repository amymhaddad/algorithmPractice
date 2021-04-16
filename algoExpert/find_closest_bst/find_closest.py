"""
https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
"""
import math 
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
 
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

def findClosestValueInBst(tree, target):
    total_values = []
    tree_values = get_tree_values(tree, total_values)
    return closest_value(tree_values, target)


def get_tree_values(tree, total_values):
    if tree is None:
        return 

    stack = [(tree, -math.inf, math.inf)]
    
    while stack:
        node, lower, upper = stack.pop()

        if node is None:
            continue

        val = node.val
        if val >= upper or val <= lower:
            continue
        total_values.append(val)
        stack.append((node.left, lower, val))
        stack.append((node.right, val, upper))
    return total_values

def closest_value(tree_values, target):
    smallest_val_so_far = tree_values[0]
    for value in tree_values:
        difference = target - value 
        if difference < 0:
            continue
        if difference < smallest_val_so_far:
            smallest_val_so_far = difference
    return smallest_val_so_far

#print(findClosestValueInBst(root, 4))

def closest(tree_values, target):
    smallest_val_so_far = tree_values[0]
    prev_difference = None

    for value in tree_values:
        current_diff = value - target
        if current_diff < 0:
            continue

        if prev_difference == None:
            prev_difference = current_diff
            continue
        
        if current_diff < prev_difference:
            prev_difference = current_diff
            smallest_val_so_far = value 
        #import pdb; pdb.set_trace()
    return smallest_val_so_far

print(closest([10, 15, 22, 13, 14, 5, 2, 1], 12))

