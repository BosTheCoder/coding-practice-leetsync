class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_win = 0
        d = {}

        for r, c in enumerate(s):
            d[c] = d.get(c,0) + 1
            
            # shrink window if invalid
            while (r - l + 1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            
            # Check if window length is the largest
            max_win = max(
                max_win,
                (r - l + 1)
            )
        
        return max_win