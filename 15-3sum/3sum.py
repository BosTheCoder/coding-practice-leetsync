class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            target = 0 - nums[i]
            j = i+1
            k = len(nums)-1

            while j<k:
                total = nums[j] + nums[k]

                if total == target:
                    ret.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif total>target:
                    k-=1
                else:
                    j+=1
        
        return ret


"""

-4 
-1 
-1 i
-1 j
0 
1 
2  




if nums[i] + nums[k] < target:

loop while j<k

avoiding duplicates:
- when you find a match move j forward to a number thats ot the same
- move forward i to a number thats not the same
"""


