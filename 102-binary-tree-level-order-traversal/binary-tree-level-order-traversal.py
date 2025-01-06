# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ret = []
        def dfs(node, level:int, arr:list):
            if not node:
                return

            if level>len(arr):
                arr.append([])

            arr[level-1].append(node.val)
            dfs(node.left, level+1, arr)
            dfs(node.right, level+1, arr)
        
        dfs(root, 1, ret)
        return ret
        