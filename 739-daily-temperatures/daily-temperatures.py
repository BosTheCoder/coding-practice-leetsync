class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [(75,2),(72,5)]
        ret = [0]*len(temperatures) # [1,1,0,2,1,0,0,0]
        for ix, temp in enumerate(temperatures): # 5,72
            while stack and stack[-1][0] < temp:
                old_temp, old_ix = stack.pop()  # 71,3
                ret[old_ix] = ix - old_ix   # 2
            stack.append((temp,ix))
        return ret


