# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node) -> tuple[bool,int]:
            if node is None:
                return True, 0
            
            lb, lh = dfs(node.left) 
            if not lb:
                return False, -1
            rb, rh = dfs(node.right) 

            return (
                lb and rb and (abs(lh-rh) <=1),
                max(lh, rh) + 1
            )
        
        return dfs(root)[0]



