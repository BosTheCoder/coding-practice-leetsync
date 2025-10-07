# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = None
        next = head
        
        while next:
            temp = next.next
            next.next = curr
            curr = next
            next = temp
        return curr
