class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        # Add all values to heap apart from last one
        for i in range(k-1):
            # making a max heap
            heapq.heappush(heap,(-nums[i],i))
        # print(f"heap is {heap}")
        ret = []
        for start in range(len(nums)-k+1):
            # add the new value to the heap
            end = start + k -1
            heapq.heappush(heap, (-nums[end],end))
            # print(f"new value {-nums[end]} added to heap. heap is now {heap}")

            # if max value in the heap is old, get rid of it
            while heap[0][1] < start:
                heapq.heappop(heap)
            
            maximum = -heap[0][0]
            ret.append(maximum)
        
        # print(ret)
        return ret



        