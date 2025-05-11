class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last, day = {}, 0
        for t in tasks:
            day += 1
            if t in last and day - last[t] <= space:   # still too soon
                day = last[t] + space + 1             # jump directly
            last[t] = day                              # record execution day
        return day
