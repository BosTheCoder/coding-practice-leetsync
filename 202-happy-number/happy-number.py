class Solution:
    def isHappy(self, n: int) -> bool:
        def getdigits(val:int) -> list:
            ret = []
            while val>=1:
                ret.append(val % 10)
                val = val//10
            return ret
        
        cycleset = set()
        while True:
            if n == 1:
                return True
            if n in cycleset:
                return False
            cycleset.add(n)
            digits = getdigits(n)
            squared_digits = [digit**2 for digit in digits]
            n = sum(squared_digits)