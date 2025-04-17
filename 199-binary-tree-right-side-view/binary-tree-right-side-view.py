# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = Deque()
        ret = []
        if not root:
            return []
        q.appendleft(root)
        nodes_on_level = 1
        while q:    # [5,4]
            nodes_on_level = len(q) # 2
            ret.append(q[-1].val)   # [1,3,4]
            for i in range(nodes_on_level): # 1
                node = q.pop()  # 2
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        return ret

        