class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = []
        for c in s:
            if c.isalnum():
                new_s.append(c)
        s = "".join(new_s)
        left = 0
        right = len(s)-1
        while left<right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        
        return True