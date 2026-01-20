class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l =0
        r = len(nums)

        while l<r:
            m = l + (r-l)//2
            if nums[m]<=nums[-1]:
                r = m
            else:
                l = m+1
        print(f"pivot is {l}")

        # If pivot is 0 just treat it as regular binary search
        if l == 0:
            x = bisect_left(nums,target)
            return x if x<len(nums) and nums[x]==target else -1

        # Figuring out which half its' in
        if nums[0] <= target <= nums[l-1]:
            x = bisect_left(nums,target,0,l)
            return x if nums[x]==target else -1
        elif nums[l] <= target <= nums[-1]:
            x = bisect_left(nums,target,l,len(nums))
            return x if nums[x]==target else -1
        else:
            return -1

"""

4  l 
5
6
-1 m
0
1 
2  r
"""