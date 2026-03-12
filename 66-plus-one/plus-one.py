class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digit = digits[i]   # 9

            digit_and_carry = digit + carry # 10

            new_val = digit_and_carry % 10  # 0
            carry = digit_and_carry // 10   # 1

            digits[i] = new_val # 0
        
        if carry:
            return [carry] + digits
        else:
            return digits


