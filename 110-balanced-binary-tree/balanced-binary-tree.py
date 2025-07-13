# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return True, 0
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            left_height += 1
            right_height+=1

            return left_balanced and right_balanced and abs(left_height - right_height) <= 1, max(left_height, right_height)
        
        balanced, height = dfs(root)

        return balanced