class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        q = Deque()
        for ix in range(len(digits)-1,-1,-1):
            num = digits[ix]
            ans = carry + num
            carry = ans // 10 
            remainder = ans % 10
            q.appendleft(remainder)
        
        if carry>0:
            q.appendleft(carry)
        
        return list(q)
"""

9 9

carry = 1

# ix 1

carry + digits[ix] = 1 + 9 = 10
carry = ans // 10 =   1
remainder = ans % 10 = 0
queue.push(remainder) = [0]

# ix 0

carry + digits[ix] = 1 + 9 = 10
carry = ans // 10 =   1
remainder = ans % 10 = 0
queue.push(remainder) = [0,0]


if carry >0
    queure.push(carry)



"""