class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        r_counts = defaultdict(list) # reverse counts
        for key,v in counts.items():
            r_counts[v].append(key)

        # start ptr at max value of reverse counts
        ptr = max(r_counts.keys())  
        ret = []
        while k and ptr>=0:
            if len(r_counts[ptr]):
                val = r_counts[ptr].pop()
                ret.append(val)
                k-=1
            else:
                ptr-=1
        return ret




