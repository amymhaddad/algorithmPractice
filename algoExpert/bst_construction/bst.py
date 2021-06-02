"""
https://www.algoexpert.io/questions/BST%20Construction
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self

        while True:
            if value < current_node:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break 
                else:
                    current_node = current_node.right
        return self 

    def contains(self, value):
        current_node = self
        
        #import pdb; pdb.set_trace()
        while current_node:
            if current_node.value == value:
                return True

            elif current_node.value > value:
                current_node = current_node.left 
            else:
                current_node = current_node.right
        return False



a = BST(10)
a.left = BST(5)
a.right = BST(15)
print(a.contains(5))
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)
#

def pre_order(root):
    if root:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)
print(pre_order(a))



