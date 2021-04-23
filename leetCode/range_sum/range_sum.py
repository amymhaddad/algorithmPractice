"""
https://leetcode.com/problems/range-sum-of-bst/
"""


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rangeSums(root, low, high):
    total = []
    traverse(root, low, high, total)

    return sum(total)


def traverse(root, low, high, total):
    if root is None:
        return

    is_valid = root.value >= low and root.value <= high

    if is_valid:
        total.append(root.value)
    if root.right is None and root.left is None:
        return

    traverse(root.left, low, high, total)
    traverse(root.right, low, high, total)


def get_range_sums():
    pass


if __name__ == "__main__":
    get_range_sums()
    root = Tree(1)
    root.left = Tree(2)
    root.left.left = Tree(3)
    root.right = Tree(4)

    print(rangeSums(root, 1, 4))
