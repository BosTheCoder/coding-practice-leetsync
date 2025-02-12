class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            if num-1 in seen:
                continue
            count = 1
            while num+count in seen:
                count += 1
            longest = max(longest, count)
        return longest


"""
-2 -1 0 1 2 3
0  1  2  3 4 5
"""
