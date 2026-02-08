# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return True
        
        return (
            self.isSameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
    
    def isSameTree(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        elif not a and b or not b and a:
            return False
        
        return (
            a.val == b.val and
            self.isSameTree(a.left, b.left) and
            self.isSameTree(a.right, b.right)
        )