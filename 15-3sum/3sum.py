class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)-1
        ret = []
        for i, num in enumerate(nums):
            # Skip the same i value to avoid duplicates
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            # Start two sum
            left = i+1
            right = length

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total == 0:
                    ret.append([nums[i], nums[left], nums[right]])

                    # Skip similar values
                    val = nums[left]
                    while nums[left] == val and left<right:
                        left+=1
                else:
                    right -= 1
        return ret
"""
[-1,0,1,2,-1,-4]

     i   l        r
[-4, -1, -1, 0, 1, 2]



     i   l                 r
[-4, -3, -1, -1, -1, 0, 1, 4]
"""