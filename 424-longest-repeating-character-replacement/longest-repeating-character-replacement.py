class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left =  0
        arr = [0]*26
        max_length = 0
        for right, c in enumerate(s):
            cix = ord(c) - ord("A")
            arr[cix] += 1

            # While the window is invalid
            while (right - left + 1) - max(arr) > k:
                left_cix = ord(s[left]) - ord("A")
                arr[left_cix] -=1
                left+=1
            
            max_length = max(max_length, right-left+1)
        
        return max_length

