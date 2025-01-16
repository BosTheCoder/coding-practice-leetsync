class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        def helper(ptr:int, curr:list, needed:int) -> None:
            if needed == 0:
                ret.append(curr.copy())
                return

            if needed < 0 or ptr>=len(candidates):
                return
            
            # take value
            curr.append(candidates[ptr])
            helper(ptr,curr,needed-candidates[ptr])
            curr.pop()

            # don't take value
            helper(ptr+1,curr,needed)

        
        helper(0,[],target)

        return ret