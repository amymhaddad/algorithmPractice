"""
https://www.algoexpert.io/questions/Branch%20Sums
"""
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

""""
Questions:
1. Does a tree have a left and right node? If not, return
2. Did I hit a leaf node? If yes, get the running sum and return it
3. Else (I'm not at a leaf node) then recur call the function in order to GET
a leaf node. Recur call each child node and pass the running sum in order to
keep track of the running sum: the sum of the nodes before it.
"""

"""
Main idea: 
-Keep track of the running sum, which is the sume of all nodes above it. 
This means I start at 0, then add the current node's value to this starting
value.

"""

def branchSums(root):
    """
    Keep track of all branch sums, and return this variable once I've calculated
    all branch sums. In order to do this calculation, then I need to set up
    another function that takes a node, running sum (ie, the sum of the nodes
    above it) and the sums array.
    Each node I pass in is a tree. 
    """

def calculate_branch_sums(node, running_value, sums):
    """
    This function is a side effect function that calculates the branch sum. It
    takes a node, running_value (ie: the sum of the nodes above it) and an
    array. 
    It runs through the three questions posed above:
    *Does a node ONLY have a left OR right node. If I only have one child,
    return
    *Did I hit a leaf node? 
    Ex: 4
       /  \
     8     9 
     8 is a leaf node bc it has no right and left node. 
     *Else: Did I hit a node w/BOTH a right and left node? Then recur call the
     function

    The aim is to keep recurring UNTIL I hit a leaf node, then append the
    running sum. 
    """
    #First question: does a node have a RIGHT and LEFT node?
    
    #Calc a NEW running sum: the CURRENT running val that's passed in PLUS the
    #value of the current node. This matters bc I'm keeping a running total of 
    #all vals seen so far
    
    #Second question: IF I hit a leaf node --> THINK: how do I know if I hit a
    #leaf (look at ex in doc string)
        #Then return the running sum (ie, the running val PLUS the current
        #node's value 
    
    #Third question: else
    #I've hit a node that has BOTH children, so recur call the function 
    #to get the left vaue and the right value
