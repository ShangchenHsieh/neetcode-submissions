# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(node, max_history): 
            if not node: 
                return 

            if node.val >= max_history: # good node
                res.append(node.val)
            

            dfs(node.left, max(max_history, node.val))
            dfs(node.right, max(max_history, node.val))


        dfs(root, root.val)
        return len(res)