from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()            # stores *indices* of nums in decreasing order
        res = []

        for i, x in enumerate(nums):
            # 1️⃣  Drop indices that slid out of the window
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2️⃣  Maintain decreasing order in dq
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            dq.append(i)

            # 3️⃣  Record a max once the first window is full
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
