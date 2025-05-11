class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = []
        
        for char, count in counts.items():
            heapq.heappush(heap,(-count,char))

        times = {}
        time = 0
        tasks_left = len(tasks)

        while tasks_left:
            for count, char in times.get(time, []):
                heapq.heappush(heap, (-count, char))
            if time in times: del times[time]

            if len(heap)!=0:
                count,char = heapq.heappop(heap)
                count = abs(count)
                tasks_left -= 1
                count -= 1
                next_time = time+n+1             


                if count > 0:
                    times.setdefault(next_time,[]).append((count,char))

            time+=1

        return time