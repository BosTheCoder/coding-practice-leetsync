# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def bs(node, l, g):
            if node.val <= g and node.val>= l:
                return node
            if node.val>g:
                return bs(node.left, l, g) 
            else:
                return bs(node.right, l, g)
        
        return bs(root, min(p.val, q.val), max(p.val, q.val))
        