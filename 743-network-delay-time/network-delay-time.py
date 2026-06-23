class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        heapq.heappush(heap,(0,k))

        adj_list = {}
        for src,dest,time in times:
            # if node isn't present yet
            if src not in adj_list:
                adj_list[src]=[(dest,time)]
            else:
                # else just append
                adj_list[src].append((dest,time))

        seen = set()

        while heap:
            curr_time, src = heapq.heappop(heap)
            if src in seen:
                continue
            else:
                seen.add(src)
            
            if len(seen) == n:
                return curr_time

            if src not in adj_list:
                continue
            
            for dest,time in adj_list[src]:
                heapq.heappush(heap, (curr_time+time, dest))

        return -1
"""
key info
- no loops
- each edfe is unique
- can you have u_i, v_i as well as v_i, u_i -> yes
- is the network defo connected -> no, when it isn't connected then return -1
- no negative weights
- does the signal send simultaneiously
- is it one indexed - > yes

steps
- initalise heap with (0,k)
- initalise adjacency list with hash map to find nodes quicker

while heap
- pop min node from heap, you end up with curr_time, node_id
- if you've seen node before skip 
- add node_id to seen
- add it's other connected nodes to the heap with (curr time + time to node, node id of connected node)


- exit loop as soon as seen contains all nodes

if exited the loop and seen does not contain all nodes
- return -1


- [ ] What is the name of the auto dict
"""