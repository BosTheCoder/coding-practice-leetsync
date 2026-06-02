class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n+1)
        for ix in range(1,len(memo)):
            target_ix = ix//2
            increment = ix%2
            num_ones = memo[target_ix] + increment
            memo[ix] = num_ones
        
        return memo
        
"""

0   0       0
1   1       1   1+memo[0]   memo[0] + 1 = 1
2   10      1   1+memo[0]   memo[1] + 0 = 1
3   11      2   1+memo[1]   memo[1] + 1 = 2
4   100     1   1+memo[0]   memo[2] + 0 = 1
5   101     2   1+memo[1]   memo[2] + 1 = 2
6   110     2   1+memo[2]   memo[3] + 0 = 2
7   111     3   1+memo[3]   ...
8   1000    1   1+memo[0]   ...


target_ix = (ix//2)
increment = ix%2

num_ones = memo[target_ix] + increment
"""