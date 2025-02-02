class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ix = -1
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i] + carry
            carry = digit // 10
            digits[i] = digit % 10
            if carry == 0:
                return digits
        digits = [carry] + digits
        return digits
