class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prev_end = float("-inf")
        intervals.sort(key=lambda x: x[1])
        total = 0
        for start,end in intervals:
            if start>= prev_end:
                prev_end = end
            else:
                total+=1
                prev_end = min(prev_end, end)
        return total