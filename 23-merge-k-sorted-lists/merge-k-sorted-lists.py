# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Wrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, Wrapper(node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            smallest = heapq.heappop(heap).node  # 1
            value_to_add = smallest.next    # 4

            # Making sure to replenish the heap 
            # We get the next one in the list
            if value_to_add:
                heapq.heappush(heap,Wrapper(value_to_add))

            # Setting up the return list
            curr.next = smallest            # 
            curr = smallest                 # 

            
        return dummy.next
        
        
"""

[[1,4,5],[1,3,4],[2,6]]

heap = 2, 4, 3

         c
dummy -> 1 -> 1
"""