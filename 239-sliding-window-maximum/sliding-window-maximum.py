from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # store indices, nums[q[0]] is max
        res = []

        for i, x in enumerate(nums):
            # evict indices left of window
            while q and q[0] <= i - k:
                q.popleft()

            # maintain decreasing deque
            while q and nums[q[-1]] <= x:
                q.pop()

            q.append(i)

            # output once first window is formed
            if i >= k - 1:
                res.append(nums[q[0]])

        return res