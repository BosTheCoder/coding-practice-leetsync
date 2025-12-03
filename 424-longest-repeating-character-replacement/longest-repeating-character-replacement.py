class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        k = 2

        """
        l = 0   # 0
        r = 0   # 0
        d = [0]*26  # {}
        max_substring = 0
        while r<len(s):
            c = s[r]
            c_val = ord(c)-ord('A')
            d[c_val] += 1

            while (r-l+1) - max(d) > k:
                c = s[l]
                c_val = ord(c)-ord('A')
                d[c_val] -= 1
                l += 1
            
            
            max_substring = max(max_substring, r-l+1)

            r += 1
        
        return max_substring

