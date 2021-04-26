"""
https://leetcode.com/problems/range-sum-of-bst/
"""


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Recur solution 1
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


# Recur sol 2
def rangeSums2(root, low, high):
    total = 0

    def traverse(node):
        nonlocal total

        if node:
            if node.value >= low and node.value <= high:
                total += node.value
            if node.value > low:
                traverse(node.left)
            if node.value < high:
                traverse(node.right)

    traverse(root)
    return total


if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(2)
    root.left.left = Tree(3)
    root.right = Tree(4)

    print(rangeSums(root, 1, 4))
    print(rangeSums2(root, 1, 4))

# Iter sol
def iter_range_sum(root, low, high):
    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        if node is None:
            return

        is_valid = node.value >= low and node.value <= high

        if is_valid:
            res.append(node.value)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return sum(res)
