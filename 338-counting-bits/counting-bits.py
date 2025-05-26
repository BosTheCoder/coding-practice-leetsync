class Solution:
    def countBits(self, n: int) -> List[int]:
        mult = 1
        ret = [0] * (n+1)
        for i in range(1, n+1):
            if mult * 2 == i:
                mult *= 2
            ret[i] = 1 + ret[i-mult]
        return ret