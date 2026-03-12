class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        max_count = max(counts.values())

        counts_to_element = defaultdict(list)

        for element,count in counts.items():
            counts_to_element[count].append(element)
        

        ret = []
        count = max_count
        while len(ret) < k:
            if count in counts_to_element:
                ret.extend(counts_to_element[count])
            count -=1

        
        return ret