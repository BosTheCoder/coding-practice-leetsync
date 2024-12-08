class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        marker = 1
        for i in range(1, n+1):
            if i == marker*2:
                marker *= 2
            # print(i, marker, dp)
            dp[i] = 1 + dp[i-marker]
            
        return dp

"""
maker = 2
when i = marker, marker *= 2

0: 0000 0
1: 0001 = 1 + dp[1-1]
2: 0010 = 1 + dp[2-2] = 1
3: 0011 = 1 + dp[3-2] = 1+1 = 2
4: 0100 = 1 + dp[4-4] = 0
5: 0101 = 1 + dp[5-4] = 2
6: 0110 = 1 + dp[6-4] = 2
7: 0111 = 1 + dp[7-4] = 3
8: 1000 = 1 + dp[8-8] = 1
9: 1001 = 1 + dp[9-8] = 2
...
"""