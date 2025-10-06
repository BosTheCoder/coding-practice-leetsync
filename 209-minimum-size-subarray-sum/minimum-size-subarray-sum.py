class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        curr = 0 
        ret = float("inf") 
        while right <len(nums):
            
            curr += nums[right]
            print(right, left,curr)
            while curr >= target:
                
                ret = min(ret, right-left+1)
                
                curr -= nums[left] 
                left += 1
                
            right += 1
        
        return ret if ret!= float("inf") else 0