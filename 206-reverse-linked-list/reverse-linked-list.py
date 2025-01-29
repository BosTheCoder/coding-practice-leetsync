# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        left = None
        curr = head
        while curr:
            right = curr.next
            curr.next = left
            left = curr
            curr = right

        return left

