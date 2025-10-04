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
        return any((
            self.sametree(root,subRoot),
            self.isSubtree(root.left, subRoot),
            self.isSubtree(root.right, subRoot)
        ))
    def sametree(self, m, s):
        if not m and not s:
            return True
        if m and not s:
            return False
        if not m and s:
            return False
        return all((
            m.val == s.val,
            self.sametree(m.left,s.left),
            self.sametree(m.right,s.right)
        ))