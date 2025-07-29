# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        return (
            self.is_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

        
    
    def is_tree(self,a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return (
            a.val == b.val 
            and self.is_tree(a.left, b.left) 
            and self.is_tree(a.right, b.right)
        )