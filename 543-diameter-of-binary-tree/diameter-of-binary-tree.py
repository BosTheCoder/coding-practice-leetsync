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
            
            # get max length and the height
            ml, hl = dfs(node.left)
            mr, hr = dfs(node.right)

            # Add 1 to the heights
            hl += 1
            hr += 1

            ret =  (
                max(ml, mr, hl + hr),
                max(hl,hr)
            )

            return ret



        return dfs(root)[0]