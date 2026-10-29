# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case: p and q are null -> balanced
        if not p and not q: # both empty
            return True
        if not p or not q: # one empty
            return False
        if p.val != q.val: # not equal
            return False

        left_balanced = self.isSameTree(p.left, q.left)
        right_balanced = self.isSameTree(p.right, q.right)

        return left_balanced and right_balanced