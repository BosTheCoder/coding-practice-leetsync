class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            char_counts = Counter(string)
            frozen_counts = tuple(sorted(tuple(char_counts.items())))
            d[frozen_counts].append(string)
        
        return list(d.values())