# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m1 = l1
        m2 = l2
        new_head = ListNode() 

        curr = new_head
        carry = 0
        while m1 or m2 or carry:
            total = 0
            if m1:
                total+=m1.val
                m1 = m1.next
            if m2:
                total+=m2.val
                m2 = m2.next
            if carry:
                total+=carry

            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)
            curr.next = new_node
            curr = new_node

        return new_head.next

"""


"""