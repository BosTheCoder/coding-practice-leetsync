class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ret = []
        for i, num in enumerate(nums):
            if i and num == nums[i-1]:
                continue
            target = 0 - num

            l, r = i+1, len(nums)-1
            while l<r:
                total = nums[l]+nums[r]
                if total > target:
                    r-=1
                elif total < target:
                    l += 1
                else:
                    ret.append([num,nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] == nums[l-1] and l <r:
                        l+=1
                    
        return ret
