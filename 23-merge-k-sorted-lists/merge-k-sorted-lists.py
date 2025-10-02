# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, node_wrapper):
        return self.node.val < node_wrapper.node.val

    def __repr__(self):
        return f"NodeWrapper(val:{self.node.val})"
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        
        # initialise heap with first node in each list
        for node in lists:
            if not node:
                continue
            
            # create wrapper and add to heap
            node_wrapper = NodeWrapper(node)
            heapq.heappush(heap, node_wrapper) 
        
        # create final list iteratively
        dummy = ListNode()
        curr = dummy
        while heap:
            node_wrapper = heapq.heappop(heap)
            node = node_wrapper.node

            # after popping add the next node back on if there is one
            if node.next:
                node_wrapper = NodeWrapper(node.next)
                heapq.heappush(heap, node_wrapper)
            
            # Add original node to the list

            curr.next = node
            curr = curr.next
        
        return dummy.next

            
        
