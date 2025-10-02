class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = (float("-inf"),0)
        half = len(nums) // 2
        store = {}
        for num in nums:
            store[num] = store.get(num,0) + 1
            if store[num] > half:
                return num
            if m[0] < store[num]:
                m = (store[num], num)
        
        return m[1]