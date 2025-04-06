# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def find_val(i,j,val):
            """Find the value in inorder[i:j+1]"""
            for ix in range(i, j+1):
                if inorder[ix] == val:
                    return ix
            raise Exception("Not found")

        def dfs(i,j,k):
            if i>j:
                return None
            if i == j:
                return TreeNode(inorder[i])
            x = find_val(i,j,preorder[k])
            curr = TreeNode(inorder[x])
            curr.left = dfs(i, x-1, k+1)
            curr.right = dfs(x+1, j, k+1+(x-i))
            return curr
        
        return dfs(0,len(preorder)-1, 0)