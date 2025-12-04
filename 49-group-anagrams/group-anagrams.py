class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for ch in string:
                counts[ord(ch) - ord("a")] += 1
            frozen_counts = tuple(counts)
            d[frozen_counts].append(string)
        
        return list(d.values())