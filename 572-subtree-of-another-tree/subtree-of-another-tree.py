# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def issame(a, b):
            if not a and not b :
                return True
            elif (a and not b) or (b and not a):
                return False
            else:
                return (
                    a.val == b.val and
                    issame(a.left, b.left) and
                    issame(a.right, b.right)
                )
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if issame(root, subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)