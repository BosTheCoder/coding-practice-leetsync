class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for ix in range(1,len(intervals)):
            if intervals[ix][0] <intervals[ix-1][1]:
                return False
        return True