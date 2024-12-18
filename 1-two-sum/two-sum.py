class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for ix,num in enumerate(nums):
            if num in needed:
                return [ix, needed[num]]
            needed[target-num] = ix
        return []