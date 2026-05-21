# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        null_node = ListNode(0,head)

        curr = null_node

        # first pass
        size = 0
        while curr.next:
            curr = curr.next
            size += 1

        # calculate which node to remove
        node_to_remove = size-n+1
        node_before_node_to_remove = node_to_remove - 1
        
        # second pass
        curr = null_node
        ix = 0

        while ix != node_before_node_to_remove:
            curr = curr.next
            ix += 1
        
        curr.next = curr.next.next

        return null_node.next



"""
               
[null,1,2,3,4,5]

"""