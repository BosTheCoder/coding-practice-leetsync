class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            bit = n & 1
            total += bit
            n >>= 1
        return total