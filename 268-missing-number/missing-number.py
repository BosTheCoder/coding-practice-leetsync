class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        n = length + 1

        curr = 0 
        for i in range(n):
            curr ^= i
        
        for num in nums:
            curr ^= num
        
        return curr