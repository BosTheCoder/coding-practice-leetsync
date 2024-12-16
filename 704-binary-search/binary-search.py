class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while abs(l-r)>1:
            mid = (l + r)//2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                l = mid
            else:
                r = mid
        if target == nums[l]:
            return l
        if target == nums[r]:
            return r
        return -1
