class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0]
        for i in range(len(nums)-1,-1,-1):
            with_val = nums[i] + dp[1]
            without_val = dp[0]

            curr_max = max(with_val, without_val)
            
            # set dp values
            dp[1] = dp[0]
            dp[0] = curr_max
        
        return dp[0]