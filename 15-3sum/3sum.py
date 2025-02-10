class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        # print(nums)
        for i, num in enumerate(nums):
            # print(nums[i])
            goal = 0 - num
            needed = set()
            for j in range (i+1, len(nums)):
                if nums[j] in needed:
                    # print(f"found {nums[i]} {goal-nums[j]} {nums[j]}")
                    ret.add((nums[i], goal-nums[j], nums[j]))
                needed.add(goal-nums[j])
        return [list(s) for s in ret]
