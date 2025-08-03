# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    class NodeWrapper:
        def __init__(self, node: ListNode):
            self.node = node
        
        def __lt__(self, other: 'NodeWrapper'):
            return self.node.val < other.node.val
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        print("starting")
        for list in lists:
            
            curr = list
            print(f"working on curr {curr}")
            while curr:
                node_wrapper = self.NodeWrapper(curr)
                heapq.heappush(heap, node_wrapper)
                curr = curr.next
        print(heap)

        head= ListNode()
        curr = head

        while heap:
            node = heapq.heappop(heap).node
            curr.next = node
            curr = curr.next
        
        curr.next = None
        
        return head.next