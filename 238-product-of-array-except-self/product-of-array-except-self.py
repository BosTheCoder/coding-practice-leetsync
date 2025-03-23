class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        backwards = [0] * len(nums)
        forwards = [0] * len(nums)
        prev = 1
        for i, num in enumerate(nums):
            backwards[i] = prev * num
            prev = backwards[i]
        
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            forwards[i] = prev * nums[i]
            prev = forwards[i]
        
        def get(l, i):
            if i >= len(l) or i < 0:
                return 1
            return l[i]

        for i in range(len(nums)):
            forwards[i] = get(forwards, i+1) * get(backwards, i-1)
        
        return forwards
