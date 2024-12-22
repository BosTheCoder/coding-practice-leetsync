# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthIterativeDfs(root)

    def maxDepthIterativeDfs(self, root) -> int:
        if not root:
            return 0
        
        stack = [(root,1)] # stack stores tuples of node,urrent depth

        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                # push child nodes onto stack
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                
        return max_depth
                

