"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


APPLE
k=2

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = defaultdict(int)
        max_length = 0
        for right, c in enumerate(s):
            counter[c]+=1

            while (right-left+1) - max(counter.values()) > k:
                counter[s[left]] -=1
                left += 1
            
            max_length = max(max_length, right-left+1)
        
        return max_length
            

