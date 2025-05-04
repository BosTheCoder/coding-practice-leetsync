"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        def dfs(node):
            if not node:
                return None
            
            newnode = Node(node.val)
            print(f"setting hashmap to {node.val} to {newnode} which has a value {newnode.val}")
            newnode.next = dfs(node.next)
            hashmap[node] = newnode
            return newnode

        newhead = dfs(head)

        oldnode = head
        newnode = newhead
        while newnode:
            newnode.random = hashmap.get(oldnode.random,None)
            print(newnode.random.val if newnode.random else None)
            oldnode = oldnode.next
            newnode = newnode.next
        return newhead
        