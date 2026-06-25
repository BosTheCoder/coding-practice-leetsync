# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node) -> tuple[bool,int]:
            """
            Returns whether node is balanced and it's max height
            """

            if not node:
                return True,0
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            return (
                (left_balanced and right_balanced and abs(left_height-right_height)<=1),
                max(left_height,right_height)+1
            )

        

        return dfs(root)[0]

"""

right and left subtrees of every node differ by at most one
everychild node is balanced


"""