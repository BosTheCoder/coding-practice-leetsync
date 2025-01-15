class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest  = 0
        start, end = 0, 0
        seen = set()
        while end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1

            seen.add(s[end])
            end += 1
            longest = max(longest, end-start)
        return longest
