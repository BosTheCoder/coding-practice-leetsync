class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # l = 0
        # r = len(nums)

        # while l<r:
        #     mid = l +(r-l)//2

        #     if nums[mid]<target:
        #         l = mid + 1
        #     else:
        #         r = mid
        
        # if l <len(nums) and nums[l]==target:
        #     return l
        # else:
        #     return -1
        

        ix = bisect.bisect_left(nums,target)

        if ix<len(nums) and nums[ix]==target:
            return ix
        else:
            return -1
