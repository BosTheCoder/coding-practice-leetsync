"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        q = Deque()
        q.appendleft((node,None))
        seen = {}

        while q:
            curr, parent = q.pop()

            # copy node
            if curr.val not in seen:
                curr_copy = Node(curr.val)
                seen[curr.val] = curr_copy
            else:
                curr_copy = seen[curr.val]
            
            # add chilrden to queue
            for neighbor in curr.neighbors:
                if neighbor.val not in seen:    
                    q.appendleft((neighbor,curr_copy))

            # do connection with parent
            if parent:
                curr_copy.neighbors.append(parent)
                parent.neighbors.append(curr_copy)

        return seen[node.val]

