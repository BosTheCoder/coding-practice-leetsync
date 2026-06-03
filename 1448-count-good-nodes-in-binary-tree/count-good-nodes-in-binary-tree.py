# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, curr_max):
            count = 0
            if not node:
                return count
            
            if node.val >= curr_max:
                count += 1
                curr_max = node.val
            
            count += dfs(node.left, curr_max)
            count += dfs(node.right, curr_max)

            return count
        
        return dfs(root, -float("inf"))