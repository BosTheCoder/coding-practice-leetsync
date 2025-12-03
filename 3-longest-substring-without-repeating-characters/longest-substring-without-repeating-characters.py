class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        counts = defaultdict(int)
        ret = 0
        for r, ch in enumerate(s):
            counts[ch] += 1

            while counts[ch] > 1:
                counts[s[l]] -= 1
                l += 1
            
            ret = max(ret, r-l+1)
        return ret
        