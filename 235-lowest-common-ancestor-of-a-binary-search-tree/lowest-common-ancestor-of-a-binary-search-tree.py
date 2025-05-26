# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p,q = q,p

        def dfs(node):
            print(node.val)
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val <= node.val and q.val >= node.val:
                return node
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
        
        return dfs(root)