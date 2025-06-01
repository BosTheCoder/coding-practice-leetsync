class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for ix, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp,ix))
                continue
            
            while stack and stack[-1][0]<temp:
                last_temp, last_ix = stack.pop()
                ret[last_ix] = ix-last_ix

            stack.append((temp,ix))

        return ret

