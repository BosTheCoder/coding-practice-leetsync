class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        d = defaultdict(lambda : 0)
        max_sub = 0
        for r, c in enumerate(s):
            d[c] += 1
            while d[c] == 2:
                d[s[l]] -=1
                l += 1
            max_sub = max(r-l+1, max_sub)
        return max_sub
