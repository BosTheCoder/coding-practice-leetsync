class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lowest = min(nums)
        largest = max(nums)
        size = largest - lowest + 1
        arr = [None] * size
        for num in nums:
            ix = num - lowest
            if arr[ix] is None:
                arr[ix] = (num,0)
            else:
                _,curr = arr[ix]
                arr[ix] = (num, curr+1)

        end = len(arr) -1
        curr = None
        while k > 0 and end >= 0:
            if arr[end] is not None:
                _, num_values = arr[end]
                while num_values > 0 and k>0:
                    k -= 1
                    curr = arr[end]
                    num_values -= 1
                k -= 1
                curr = arr[end]
            end -= 1
        return curr[0]



