class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while r>l:
            m = l + (r-l)//2
            print(m)
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        
        return l




"""
1 
3 
4 
5 l
5
5 r



"""