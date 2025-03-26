class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = True
        for i in range(len(nums)-2,-1,-1):
            val = False
            for j in range(1, nums[i]+1):
                # print(nums[i+j], i, j)
                if i+j>=len(nums):
                    break
                if nums[i+j] == True:
                    # print('hoory')
                    val = True
                    break
            nums[i] = val
        # print(nums)
        return bool(nums[0])
        

"""
[2,3]
"""