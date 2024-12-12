# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursive(curr):
            if not curr or not curr.next:
                return curr

            new_head = recursive(curr.next)
            curr.next.next = curr
            return new_head
        
        h = recursive(head)
        if head:
            head.next = None
        return h
