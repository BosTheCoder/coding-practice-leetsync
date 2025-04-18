class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_window = 0
        left = right = 0
        num_zeros = 0
        while left<=right and right < len(nums):
            if nums[right] == 0:
                num_zeros += 1
            
            while num_zeros>k and left<=right:
                left+=1
                if nums[left-1] == 0:
                    num_zeros-=1
            
            right+=1
            
            max_window = max(max_window, right-left)
        return max_window
                



"""
3 1s
4 1s


2 1s
3 1s
2 1s
4 1s
"""