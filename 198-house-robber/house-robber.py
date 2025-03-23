class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        dp[0] = nums[0]
        if len(nums) < 2:
            return dp[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(dp)):
            temp = nums[i] if i <len(nums) else 0
            dp[i] = max(
                dp[i-2] + temp,
                dp[i-1]
            )
        return dp[len(nums)]