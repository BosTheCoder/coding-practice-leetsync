class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x= bisect.bisect_right(nums, target)
        # print(x)
        if x-1>len(nums) or nums[x-1]!=target:
            return -1
        return x-1