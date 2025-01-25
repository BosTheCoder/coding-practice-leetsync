class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ix,num in enumerate(nums):
            if num in d:
                return [d[num],ix]
            d[target-num] = ix
        
        return []