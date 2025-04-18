class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ref_word = "balloon"
        ref_counts = Counter(ref_word)
        counts = Counter(text)

        # adjust counts
        for c, count in ref_counts.items():
            counts[c] = counts.get(c,0)//count

        return min(counts.get(c,0) for c in ref_word)


