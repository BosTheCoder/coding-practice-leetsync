class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        size = max(c.values())
        arr = [None] * (size+1)
        for num, counts in c.items():
            arr[counts] = [num] if not arr[counts] else arr[counts] + [num]
        
        ret = []
        for i in range(size, -1, -1):
            if not arr[i]: continue

            for val in arr[i]:

                ret.append(val)
                if len(ret) >= k:
                    return ret
        