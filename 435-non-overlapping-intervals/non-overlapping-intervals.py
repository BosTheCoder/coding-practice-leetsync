class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],x[1]))
        removal_count = 0
        last_interval = intervals[0]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] < last_interval[1]:
                removal_count += 1
                last_interval = interval if interval[1]<last_interval[1] else last_interval
            else:
                last_interval = interval
        return removal_count

