class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        
        for num in range(0, len(nums)+1):
            curr ^= num
        
        return curr