class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [float("inf")] * len(temperatures)
        seen = {}
        for i in range(len(temperatures)-1,-1,-1):
            temp = temperatures[i]
            for j in range(temp+1,101):
                if j in seen:
                    ret[i] = min(ret[i],seen[j] - i)
            ret[i] = 0 if ret[i] == float("inf") else ret[i]
            seen[temp] = i
        return ret
                    
"""
            
73,74,75,71,69,72,76-(76,0),73-(73,0)

"""