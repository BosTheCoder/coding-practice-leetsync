class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = Counter(nums)
        max_count = float("-inf")
        for val, count in counts.items():
            max_count = max(max_count, count)
        
        arr = [None] * (max_count+1)
        for val, count in counts.items():
            arr[count] = arr[count] + [val] if arr[count] else [val]

        ret = []
        i = max_count
        while len(ret) < k:
            while arr[i] and len(ret) < k:
                ret.append(arr[i].pop())
            i -= 1
        return ret