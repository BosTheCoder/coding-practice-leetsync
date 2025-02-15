class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i,num in enumerate(nums):
            if num not in seen:
                seen[num] = i
                continue
            
            j = seen[num]
            if abs(i - j) > k:
                seen[num] = i
            else:
                return True
        return False 
            