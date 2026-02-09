class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find rotation point
        l,r = 0, len(nums)
        while l<r:
            mid = l + (r-l)//2
            if nums[mid] <= nums[-1]:
                r = mid
            else:
                l = mid+1
        
        # figure out which half it might be in
        
        if target >= nums[l] and target <= nums[-1]:
            ix = bisect.bisect_left(nums, target, l, len(nums))
        elif target >= nums[0]:
            ix = bisect.bisect_left(nums,target,0, l)
        else:
            return -1
        return (
            ix 
            if ix<len(nums) and nums[ix] == target
            else -1
        )

    

"""
p(x)
False,false,true,true


x < nums[-1]

"""