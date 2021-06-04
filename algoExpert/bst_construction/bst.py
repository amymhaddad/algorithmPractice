"""
https://www.algoexpert.io/questions/BST%20Construction
"""

#Iterative approach
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


#Recursive approach
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insertion(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insertion(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insertion(value)