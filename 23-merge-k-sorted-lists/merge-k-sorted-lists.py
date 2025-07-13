# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode(ListNode):
    def __init__(self, node):
        super().__init__(node.val, node.next)
    
    def __lt__(self, heap_node):
        return self.val < heap_node.val


class Solution:
    


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        curr = dummy = ListNode()
        
        for node in lists:
            if node is None:
                continue
            
            heap_node = HeapNode(node)
            heapq.heappush(heap, heap_node)
        

        while heap:
            next = heapq.heappop(heap)

            # add the nodes next value to the heap
            if next.next is not None:
                heapq.heappush(heap, HeapNode(next.next))
            
            # update pointers
            curr.next = next
            curr = next
        
        return dummy.next

        