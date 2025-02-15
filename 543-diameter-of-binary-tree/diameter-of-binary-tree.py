# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1,-1
            
            left_with_node, left_without_node = dfs(node.left)
            right_with_node, right_without_node = dfs(node.right)
            
            x=  max(left_with_node+1, right_with_node+1), max(left_without_node, right_without_node, left_with_node + right_with_node + 2)
            # print(f"For node {node.val} we have {x}")
            return x
        
        a,b = dfs(root)
        return max(a,b)
        