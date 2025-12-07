class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        if len(counts) <= k:
            return list(counts.keys())

        max_val = max(counts.values())
        arr = [ [] for i in range(max_val+1)]

        for key,v in counts.items():
            arr[v].append(key)
        
        ret = []
        for i in range(len(arr)-1,-1,-1):
            if not arr[i]:
                continue
            
            ret.extend(arr[i])
            # print("ret",ret)
            if len(ret) == k:
                return ret
        
        return ret
