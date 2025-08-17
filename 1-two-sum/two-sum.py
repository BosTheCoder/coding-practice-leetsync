class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ix,num in enumerate(nums):
            if num not in seen:
                seen[target-num] = ix
                continue
            return seen[num], ix
        return None