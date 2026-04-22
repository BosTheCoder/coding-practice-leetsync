class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum element via binary search
        # [3,1]
        # [1,3]

        l, r = 0, len(nums)     # 1,1

        while l<r:
            mid = l + (r-l)//2  # 0

            if nums[mid] <= nums[-1]:   # Yes
                r = mid     # 1
            else:
                l = mid + 1 # 1
        
        # at this point left should equal the minimum element

        # Figure out if the target is in the left or right list

        if nums[0] <= target <=nums[max(l-1,0)]:
            ix = bisect_left(nums, target, 0,l)
        elif nums[l]<= target <= nums[-1]:
            ix = bisect_left(nums, target, l) 
        else:
            return -1
        
        if ix < len(nums) and ix>=0 and nums[ix] == target:
            return ix
        else:
            return -1