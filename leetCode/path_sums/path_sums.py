"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
"""


def pathSums(root, targetSum):
    path_sums = []
    calc_path_sums(root, path_sums, 0)
    return any(val == targetSum for val in path_sums)


def calc_path_sums(root, path_sums, current_val):
    if root is None:
        return

    current_val += root.val

    if root.left is None and root.right is None:
        path_sums.append(current_val)
        return

    calc_path_sums(root.left, path_sums, current_val)
    calc_path_sums(root.right, path_sums, current_val)
