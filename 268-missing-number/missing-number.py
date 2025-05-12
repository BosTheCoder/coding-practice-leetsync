class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        # xor all nums in the array
        for num in nums:
            curr ^= num
        
        # xor for all nums in the range 0..len(nums)+1
        for i in range(len(nums)+1):
            curr ^= i

        return curr