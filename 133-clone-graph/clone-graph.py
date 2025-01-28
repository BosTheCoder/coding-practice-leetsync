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
        seen = {}

        def dfs(curr):
            if curr.val in seen:
                return seen[curr.val]
            new_node = Node(curr.val)
            seen[curr.val] = new_node
            new_neighbors = [dfs(neighbor) for neighbor in curr.neighbors]
            new_node.neighbors = new_neighbors
            return new_node
        
        return dfs(node) if node else node