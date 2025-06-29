from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val  = val
        self.next = next
    def __lt__(self, other):          # needed only if you store nodes directly
        return self.val < other.val

class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        dummy = ListNode()             # sentinel head
        tail  = dummy
        heap  = []                     # (value, list_index, node)

        # 1. Seed the heap with the first node of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        # 2. Pop the smallest current node, push its successor
        while heap:
            val, i, node = heappop(heap)
            tail.next = node           # append to merged list
            tail      = tail.next
            if node.next:              # put next element from the same list into heap
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next
