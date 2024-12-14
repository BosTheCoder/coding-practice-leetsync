# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> tuple[int,bool]:
            if not node:
                return -1, True
            height_left, bal_left = dfs(node.left)
            height_right, bal_right = dfs(node.right)
            max_height = max(height_left, height_right)
            if abs(height_left - height_right) > 1:
                return 1+max_height, False
            if not (bal_left and bal_right):
                return 1+max_height, False
            
            return 1+max_height, True
        
        h,b = dfs(root)
        return b
            

