class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        failure = set()
        def backtrack(i, left_total, right_total) -> bool:
            if (i, left_total) in failure or i>=len(nums) or left_total > right_total:
                return False
            if left_total == right_total:
                return True
            
            # Take value
            take = backtrack(i+1, left_total + nums[i], right_total - nums[i])
            if take:
                return True
            # Don't take value
            dont_take = backtrack(i+1, left_total, right_total)
            if not dont_take:
                failure.add((i, left_total))
            return dont_take

        return backtrack(0, 0, sum(nums))