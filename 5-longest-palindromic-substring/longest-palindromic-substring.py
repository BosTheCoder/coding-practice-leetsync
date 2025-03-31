class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i) -> str:
            original = i

            i = original-1
            j = original + 1
            # length is odd
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            curr = (i+1,j)
            

            # length is even
            i = original
            j = original + 1
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            # print(i+1, j)
            if curr[1] - curr[0] > j-i-1:
                return s[curr[0]: curr[1]]
            else:
                return s[i+1:j]
        
        longest = ""
        for i,c in enumerate(s):
            curr = expand(i)
            longest = longest if len(longest) > len(curr) else curr

        return longest