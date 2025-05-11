class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = []
        
        for char, count in counts.items():
            heapq.heappush(heap,(-count,char))

        times = {}
        ret = []

        time = 0
        tasks_left = len(tasks)
        while tasks_left:
            for count, char in times.get(time, []):
                heapq.heappush(heap, (-count, char))
            if time in times: del times[time]

            # print(heap)

            if len(heap) == 0:
                ret.append(None)
            else:
                count,char = heapq.heappop(heap)
                count = abs(count)

                ret.append(char)
                tasks_left -= 1
                count -= 1
                next_time = time+n+1             


                if count > 0:
                    times.setdefault(next_time,[]).append((count,char))


            time+=1
        # print(ret)
        return time