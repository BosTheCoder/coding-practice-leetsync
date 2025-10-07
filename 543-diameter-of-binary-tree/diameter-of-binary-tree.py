# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0,0 # max height, max diameter
            
            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)
            return (
                max(lh, rh) + 1,
                max(
                    ld,
                    rd,
                    lh + rh + 1
                )
            )


            
            """
            its either max height left + max height right
            or its the max diameter at left node or max diameter at right node
            """

        
        _, d = dfs(root)
        return d-1