class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        temp = prev = prevprev = 0
        for i in range(len(nums)-2, -1, -1):
            temp = max(nums[i] + prevprev, prev)
            prevprev, prev = prev, temp
        max_starting_on_0 = temp


        temp =prev = prevprev = 0
        for i in range(len(nums)-1, 0, -1):
            temp = max(nums[i] + prevprev, prev)
            prevprev, prev = prev, temp
        max_starting_on_1 = temp

        return max(max_starting_on_0, max_starting_on_1)