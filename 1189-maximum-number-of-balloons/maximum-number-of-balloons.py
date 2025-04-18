class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        instances = 0
        while True:
            found = True
            for c in "balloon":
                counts[c] = counts.get(c,0) -1
                if counts[c] <0:
                    found = False
            if found:
                instances += 1
            else:
                break
        return instances


