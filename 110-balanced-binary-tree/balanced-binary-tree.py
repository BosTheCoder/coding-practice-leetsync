# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if not node:
                return 0, True
            
            rh, rb = dfs(node.right)
            if not rb:
                return 0, False

            lh, lb = dfs(node.left)
            if not lb:
                return 0, False

            val = (
                max(rh, lh) + 1,
                abs(rh-lh) <= 1
            )
            return val
        
        _, bal = dfs(root)
        return bal
