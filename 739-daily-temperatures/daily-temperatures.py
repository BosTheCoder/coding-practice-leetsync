class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for ix, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, old_ix = stack.pop()
                ret[old_ix] = ix - old_ix
            
            stack.append((temp, ix))
        
        return ret