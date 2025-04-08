class Solution:
    def rob(self, nums: List[int]) -> int:
        curr = prev = prevprev = 0

        for i in range(len(nums)-1, -1, -1):
            curr = max(nums[i] + prevprev, prev)
            prevprev = prev
            prev = curr
        return curr