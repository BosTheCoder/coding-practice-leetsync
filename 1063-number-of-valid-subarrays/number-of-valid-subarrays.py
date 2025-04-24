class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        count = 0
        for left in range(len(nums)):
            for right in range(left,len(nums)):
                # print(left, right, nums[left], nums[right])
                if nums[left]>nums[right]:
                    break
                # print(nums[left:right+1])
                count+=1
        return count