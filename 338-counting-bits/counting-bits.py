class Solution:
    def countBits(self, n: int) -> List[int]:
        mult = 2
        count = 0
        ret = [0] * (n+1)
        for i in range(1,n+1):
            if i == mult:
                mult*=2
                count =0
        
            ret[i] = 1 + ret[count]
            count += 1
            
            
        return ret