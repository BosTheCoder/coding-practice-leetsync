class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n+1)
        mult = 1
        counter = 0
        for i in range(1, n+1):
            if counter == mult:
                mult *= 2
                counter = 0
            
            ret[i] = 1 + ret[counter]

            counter+=1
        
        return ret