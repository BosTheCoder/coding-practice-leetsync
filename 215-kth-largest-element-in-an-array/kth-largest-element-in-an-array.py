class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        arr = [0] * (max_val - min_val + 1)

        for num in nums:
            arr[num-min_val] +=1
        

        for i in range(max_val-min_val, -1, -1):
            k-=arr[i]
            if k <=0:
                return i+min_val
        return 0

