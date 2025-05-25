class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[tuple[int,int]] = []
        ret = [0] * len(temperatures)

        for ix, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                old_ix = stack[-1][1]
                ret[old_ix] = ix - old_ix
                stack.pop()

            stack.append((temp,ix))
        
        while stack:
            _, ix = stack.pop()
            ret[ix] = 0
        
        return ret

"""


"""