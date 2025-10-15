class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n>0:
            lsb = n & 1
            total += lsb
            n >>= 1
        return total