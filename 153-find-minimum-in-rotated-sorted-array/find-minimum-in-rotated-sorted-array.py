class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = l + (r-l)//2

            if nums[l] > nums[mid]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                break

        return nums[l]

"""

4 
5 
6 
7 
0 l
1 m
2 r


3 l
4 
5 
1 l m
2 r

11
13 
15 
0 rl

"""