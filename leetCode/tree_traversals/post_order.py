"""

"""

from stack import Stack


class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Tree(1)
root.left = Tree(2)
root.left.left = Tree(3)
root.right = Tree(4)

# v1 post_order
def post_order_v1(root):

    if root is None:
        return

    if root == []:
        return []

    s1 = Stack()
    s2 = Stack()
    s1.push(root)
    results = []

    while not s1.is_empty():
        root = s1.pop()
        s2.push(root)
        if root.left is not None:
            s1.push(root.left)
        if root.right is not None:
            s1.push(root.right)

    while not s2.is_empty():
        item = s2.pop()
        results.append(item.val)
    return results


# v2 post_order
def post_order_v2(root):
    traverse = []
    stack = [root]
    while stack:
        root = stack.pop()

        traverse.append(root.val)

        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)

    traverse.reverse()
    return traverse
