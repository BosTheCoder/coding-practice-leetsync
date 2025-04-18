class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        lowest = curr = 0
        for i, num in enumerate(nums):
            curr += num
            lowest = min(curr,lowest)
        return abs(lowest)+1
