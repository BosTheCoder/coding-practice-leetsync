class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # [-4,-1,-1,-1,0,1,2,2,2,3]
        ret = set()
        for i,num in enumerate(nums):   #1,-1
            target = -num   # 1
            hash = {}   # {2:-1, 1:0, }
            curr = None
            for j in range(i+1, len(nums)): # 6
                curr = nums[j]  # 2
                if curr in hash:   
                    ret.add((num, hash[curr], curr))
                else:
                    needed = target - curr  # 
                    hash[needed] = curr
            
        return [list(r) for r in ret]
                    

"""
[-1,0,1,2,-1,-4, -1]



"""