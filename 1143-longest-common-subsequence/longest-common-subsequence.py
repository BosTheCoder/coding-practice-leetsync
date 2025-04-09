class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Using the length of text2 for the memoisation array so we want the smallest text1 to save space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        memo = [0] * (len(text1) + 1)
        for i in range(len(text2)-1, -1, -1):
            curr = [0] * (len(text1) + 1)
            for j in range(len(text1)-1, -1, -1):
                val = 1 if text2[i]==text1[j] else 0
                curr[j] = max(curr[j+1], memo[j], val+memo[j+1])
            memo = curr
        
        return curr[0]

"""
abcde
ace

we can take both i & j
move i forward 1
move j forward 1

if you take you have to move both i & j forward and increment counter


"""