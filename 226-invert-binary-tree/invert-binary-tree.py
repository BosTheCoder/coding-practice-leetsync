# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a):
            if a is None:
                return a

            a.left, a.right = dfs(a.right), dfs(a.left)
            return a
        
        return dfs(root)