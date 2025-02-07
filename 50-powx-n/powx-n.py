class Solution:
    def myPow(self, x: float, n: int) -> float:
        def bin_exp(exp):
            if exp == 0:
                return 1
            if exp == 1:
                return x
            
            if exp % 2 == 0:
                curr = bin_exp(exp/2)
                return curr * curr
            
            return x * bin_exp(exp-1)
        
        isFlipped = False
        if n <0:
            n = abs(n)
            isFlipped = True
        res= bin_exp(n)
        return 1/res if isFlipped else res
                
        