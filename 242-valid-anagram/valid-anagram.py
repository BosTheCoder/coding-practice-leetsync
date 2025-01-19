class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        counts_2 = Counter(t)
        return counts == counts_2