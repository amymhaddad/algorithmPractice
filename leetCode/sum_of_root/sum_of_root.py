"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        totals = []
        helper(root, totals, start="")
        return sum(totals)


def helper(root, totals, start):
    if root is None:
        return
    start += str(root.val)
    if root.right is None and root.left is None:
        dec = int(start, 2)
        return totals.append(dec)
    helper(root.left, totals, start)
    helper(root.right, totals, start)
