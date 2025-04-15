class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        def dfs(i,curr,pos_left):
            if i >= len(nums):
                ret.append([i for i in curr])
                return
            
            pos_left_copy = tuple(pos_left)
            for p in pos_left_copy:
                curr[p] = nums[i]
                pos_left.remove(p)
                dfs(i+1,curr,pos_left)
                pos_left.add(p)
                curr[p]==None

        
        dfs(0,[None] * len(nums),{i for i in range(len(nums))})
        return ret
