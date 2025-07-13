class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ret = [intervals[0]]

        for interval in intervals:
            prev = ret[-1]
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                ret.append(interval)
        return ret