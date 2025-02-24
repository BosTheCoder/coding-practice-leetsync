# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0
            
            left_balanced, left_height = dfs(node.left)
            if not left_balanced:
                return False, -1
            
            right_balanced, right_height = dfs(node.right)
            if not right_balanced:
                return False, -1

            # print(node.val, "left", (left_balanced, left_height), "right", (right_balanced, right_height))

            return abs(left_height - right_height) <= 1, max(left_height, right_height)+1
        ret, _ = dfs(root)
        return ret
