class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(num):
            digits = [int(d)*int(d) for d in list(str(num))]
            return sum(digits)
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = squares(n)
        
        return True


        
