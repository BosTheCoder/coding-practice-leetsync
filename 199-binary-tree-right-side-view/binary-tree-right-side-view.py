# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return []
        q = Deque([root])
        while q:
            # get the last number and add to ret
            ret.append(q[-1].val)

            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ret
        

"""
bfs
ret = []
#levl 1
[1]
get last number and add to ret [1]
can see only one node
for i in range(1)
popleft and append nodes children

# lvl 2
[2,3]
get the last number and add to ret [1,3]
for i in range(2)
popleft and append nodes children
[3,4]
[4]

#lvl 3
[4]
get the last number and add to ret [1,3,4]


...

ends when queue is empty



"""