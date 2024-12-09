class Solution:
    def climbStairs(self, n: int) -> int:
        dp = deque([1,1])
        for i in range(2, n+1):
            steps_required = dp[0] + dp[1]
            dp.popleft()
            dp.append(steps_required)
        return dp[1]
