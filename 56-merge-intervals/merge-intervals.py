class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = [intervals[0].copy()]

        for curr in islice(intervals,1, None):
            last = ret[-1]
            if curr[0] <= last[1]:
                last[1] = max(last[1],curr[1])
            else:
                ret.append(curr.copy())

        return ret
            