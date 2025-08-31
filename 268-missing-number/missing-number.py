class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        curr = 0
        for num in nums:
            curr ^= num
        for i in range(n+1):
            curr ^= i
        return curr