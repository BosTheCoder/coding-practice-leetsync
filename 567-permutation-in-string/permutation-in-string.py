class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        target = dict(Counter(s1))
        curr = {}
        for r, ch in enumerate(s2):
            # print()
            # print(f"l {l} r {r} ch {ch}")
            curr[ch] = curr[ch] + 1 if ch in curr else 1
            # print("curr",curr)

            if r-l+1 != len(s1):
                # print(f"continuing win length {r-l+1} not equal to {len(s1)}")
                continue
            
            if curr != target:
                # print(f"curr {curr} != {target}")
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                    del curr[s2[l]]
                l += 1
            else:
                return True
            
        
        return False





