"""
https://www.algoexpert.io/questions/BST%20Construction
"""

# Iterative approach
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right

    def contains(self, value):
        current = self

        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False


#
# Recursive approach
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertion(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insertion(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insertion(value)

    def contains(self, value):
        if self.value > value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif self.value < value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True


a = BST(10)
a.left = BST(5)
a.right = BST(15)
a.insertion(12)
print(a.contains(112))


def pre_order(a):
    if a:
        print(a.value)
        pre_order(a.left)
        pre_order(a.right)


print(pre_order(a))
