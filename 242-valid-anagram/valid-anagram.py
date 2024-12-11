class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        base = ord("a")
        for c in s:
            arr[ord(c)-base] += 1
        for c in t:
            arr[ord(c)-base]-=1
        
        for num in arr:
            if num:
                return False
        return True