class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        q = Deque()
        for i in range(len(digits)-1,-1,-1):
            digit = digits[i]
            digit += carry

            carry = max(digit - 9,0)
            digit = digit % 10

            q.appendleft(digit)
        
        if carry:
            q.appendleft(carry)
        
        return list(q)