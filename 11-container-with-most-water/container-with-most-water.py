class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ret = 0
        while l<r:
            length = r-l
            if height[l]<height[r]:
                curr_height = height[l] * length
                l+=1
            else:
                curr_height = height[r] * length
                r-=1
            ret = max(ret, curr_height)
        return ret