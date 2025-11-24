class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            s = str(n)
            sq = [int(c)*int(c) for c in s]
            su = sum(sq)
            print(su)
            if su == 1:
                return True
            if su in seen:
                return False
            seen.add(su)
            n = su
        return False