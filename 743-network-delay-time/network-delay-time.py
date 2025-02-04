class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # convert to adj list
        adj_list = {}
        for source, target, time in times:
            if source not in adj_list:
                adj_list[source] = []
            adj_list[source].append((time,target))
        
        all_nodes = set(range(1,n+1))
        seen  = set()
        heap = []
        heapq.heappush(heap,(0, k))
        while heap:
            time, node = heapq.heappop(heap)
            if node not in seen:
                seen.add(node)
            else:
                continue
            if seen == all_nodes:
                return time
            for t, n in adj_list.get(node,[]):
                heapq.heappush(heap,(t+time, n))
        return -1



