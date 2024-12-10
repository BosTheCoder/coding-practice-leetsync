class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        mask = 1
        for i in range(31):
            ans |= (n & mask)
            n >>= 1
            ans <<= 1
        ans |= (n & mask)
        return ans