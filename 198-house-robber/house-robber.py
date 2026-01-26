class Solution:
    def rob(self, nums: List[int]) -> int:
        including = 0
        not_including = 0

        for i in range(len(nums)-1,-1,-1):
            new_including = nums[i] + not_including
            new_not_including = max(including, not_including)

            including = new_including
            not_including = new_not_including
        
        return max(including, not_including)

"""





"""