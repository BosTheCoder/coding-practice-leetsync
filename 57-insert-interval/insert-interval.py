class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # newInterval = 1,5
        
        ret = [] # 
        added = False
        for interval in intervals: # 6,9

            if added or interval[1] < newInterval[0]:
                # if interval is clearly first
                ret.append(interval)
            elif interval[0] > newInterval[1]:
                # new interval needs to go before this interval
                ret.append(newInterval)
                ret.append(interval)
                added = True
            elif interval[0] <= newInterval[1] and interval[1] >= newInterval[0]:
                newInterval = [
                    min(interval[0],newInterval[0]), 
                    max(interval[1],newInterval[1])
                ]
        
        if not added:
            ret.append(newInterval)

        return ret


            
"""
ret = 

interval 
new interval = 
"""