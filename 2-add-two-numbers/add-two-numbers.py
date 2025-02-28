# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = head = ListNode()
        carry = 0
        while l1 or l2:
            # Create new node
            head.next = ListNode()
            head = head.next

            add = carry
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next

            carry = add //10
            digit = add % 10

            head.val = digit

        if carry:
            head.next = ListNode(carry)
            head = head.next

        return ret.next

