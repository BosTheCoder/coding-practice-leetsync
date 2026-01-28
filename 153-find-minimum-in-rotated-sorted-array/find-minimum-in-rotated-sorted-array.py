class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)

        while l<r:
            m = l + (r-l)//2

            if nums[m]<=nums[-1]:
                r=m
            else:
                l=m+1

        return nums[l]

"""
3 
4
5 
1 l
2 m
  r

"""