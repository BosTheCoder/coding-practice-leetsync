class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(ix: int, curr: int, symbol: str = "+") -> int:
            if ix >= len(nums):
                return 1 if curr == 0 else 0
            
            if (ix, curr) in memo:
                return memo[(ix,curr)]
            # print("ix",ix, "nums[ix]", nums[ix],"curr",curr, symbol)
            ans= helper(ix + 1, curr - nums[ix], "+") + helper(ix + 1, curr + nums[ix], "-")
            memo[(ix,curr)] = ans
            return ans
        
        return helper(0, target)
        
