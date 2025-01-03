class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ret = []
        if not intervals or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        i, j = 0, 1
        while j < len(intervals):
            curr_interval = intervals[i]
            while j < len(intervals) and curr_interval[1] >= intervals[j][0]:
                curr_interval[1] = max(curr_interval[1], intervals[j][1])
                j+=1
                

            ret.append(curr_interval)
            i = j
        
        return ret
"""
 ij
[0,2],[1,4],[3,5]
"""