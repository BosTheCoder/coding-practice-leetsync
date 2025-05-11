class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # tasks = 5,8,8,5, len(tasks)=4, space =2
        map = {} # {5:8, 8:7}
        day = 0 # 6
        i=0 # 4
        while i <len(tasks):
            task = tasks[i] # 5
            ready = map.get(task,-1)   # 3

            day = max(day,ready)  # 5
            map[task] = max(day+space+1, ready) # 8
            
            day += 1
            i+=1
        return day




"""
i   
1,2,1,2,3,1
day = 0
s = 3
q=(1,4),(2,5)


if q[0]
q.append((task,next_day))
"""