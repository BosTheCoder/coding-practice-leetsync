class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Finding the pivot
        l = 0 
        r = len(nums)

        while l<r:
            m = l+(r-l)//2

            if nums[m]<nums[0]:
                r = m
            else:
                l = m+1
        
        if l==len(nums):
            l = 0
        
        # Right now L contains the smallest number
        # Value could be in either half

        if target >= nums[l] and target<=nums[len(nums)-1]:
            i = bisect_left(nums,target,l)
        else:
            i = bisect_left(nums,target,0,l)

        return i if i<len(nums) and nums[i]==target else -1


"""

false, false, false, true...

[4,5,6,7,0,1,2]

p = lambda x: x < nums[0]


[1,2,3,4]

[4,1,2,3]


[3,1]


"""