# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(a, b) -> bool:
            if not a and not b:
                return True
            if (not a and b) or (not b and a):
                return False
            
            if a.val == b.val:
                return same_tree(a.left,b.left) and same_tree(a.right, b.right)
            
            return False

        def dfs(a, b):
            if not b:
                return True
            if not a:
                return False
    
            return same_tree(a,b) or dfs(a.left,b) or dfs(a.right, b)
            
        return dfs(root, subRoot)
