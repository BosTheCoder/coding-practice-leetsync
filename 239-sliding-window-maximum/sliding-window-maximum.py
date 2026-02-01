class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        i = j = 0
        q = Deque()

        while j<len(nums):
            # Shorten window
            if j-i == k:
                if q and q[0] == nums[i]:
                    q.popleft()
                i += 1

            # Add new value
            while q and nums[j] > q[-1]:
                q.pop()
            q.append(nums[j])

            # Get max
            if (j+1)-i == k:
                ret.append(q[0])
            
            # move forward
            j += 1
        
        return ret