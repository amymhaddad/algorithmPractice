"""
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1003/
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertion_bst(self, value):
        #Start at the root node BUT wnat to keep track of where we are at 
        current = self
        
        while True:
            #I can do the checks right here -- IF this is cond is T, then do the check right here
            if current.value <= value:
                if current.left is None:
                    #Create a link on the tree by creating an instance of hte BST calss 
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
                
        return self


# root = TreeNode(10)
# root.left = TreeNode(2)
# root.right = TreeNode(14)
# #root.left.left = TreeNode(1)


new_value = 1




def pre_order(x):
    import pdb; pdb.set_trace()
    while x:
        print(x.val)
        pre_order(x.left)
        pre_order(x.right)

         

