"""
https://www.algoexpert.io/questions/Branch%20Sums
"""
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, running_value, sums):
    if node is None:
        return

    new_running_value = running_value + node.value
    if node.right is None and node.left is None:
        sums.append(new_running_value)
        return
    calculate_branch_sums(node.left, new_running_value, sums)
    calculate_branch_sums(node.right, new_running_value, sums)
