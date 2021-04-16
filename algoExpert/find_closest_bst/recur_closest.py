import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)


def findClosestValueInBst(tree, target):
    total_values = []
    tree_values = get_tree_values(tree, total_values)
    return closest_value(tree_values, target)


def get_tree_values(node, total_values):
    def node_values(node, total_values, lower=-math.inf, upper=math.inf):
        if node is None:
            return total_values
        if node.value >= upper or node.value <= lower:
            return total_values
        total_values.append(node.value)
        return node_values(node.left, total_values, lower, node.value) and node_values(
            node.right, total_values, node.value, upper
        )

    return node_values(node, total_values)


def closest_value(tree_values, target):
    smallest_val_so_far = tree_values[0]
    prev_difference = None

    for value in tree_values:
        curr_difference = abs(value - target)
        if prev_difference == None:
            prev_difference = curr_difference
            continue
        if curr_difference < prev_difference:
            prev_difference = curr_difference
            smallest_val_so_far = value
    return smallest_val_so_far
