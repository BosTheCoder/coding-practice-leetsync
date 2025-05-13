class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        width, height = len(word2)+1, len(word1)+1
        memo = [[0]*width for _ in range(height)]

        # fill in edges
        for i in range(width-1):
            memo[height-1][i]= width-1-i
        
        for j in range(height-1):
            memo[j][width-1] = height-1-j
        
        # go right to left and fill in gaps

        for j in range(height-2,-1,-1):
            for i in range(width-2,-1,-1):
                memo[j][i] = min(
                    1 + memo[j+1][i+1],
                    1 + memo[j+1][i],
                    1 + memo[j][i+1],
                )  if word1[j] != word2[i] else memo[j+1][i+1]
        return memo[0][0]