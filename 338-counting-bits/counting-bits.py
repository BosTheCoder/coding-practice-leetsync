class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n+1)
        nextstep = 2
        delta = 0
        for i in range(1, n+1):
            if i == nextstep:
                delta = nextstep
                nextstep *= 2

            ret[i] = 1 + ret[i-delta] 
        
        return ret