class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ret = [0] * (n+1) 
        target = 1 
        counter = 0 
        for i in range(1,n+1):
            if counter == target:   
                target *= 2
                counter = 0
        
            ret[i] = 1 + ret[counter]

            counter += 1
        
        return ret


        
"""
0 0
1 1    = 1 + m[0]    = bin(1) + m[0]
2 10   = 10 + m[0]   = bin(2) + m[0]
3 11   = 10 + m[1]   = bin(2) + m[1]
4 100  = 100 + m[0]  = bin(4) + m[0]
5 101  = 100 + m[1]  = bin(4) + m[1]
6 110  = 100 + m[2]  = bin(4) + m[2]
7 111  = 100 + m[3]  = bin(4) + m[3]
8 1000 = 1000 + m[0] = bin(8) + m[0]
9 1001
10 1010
11 1011
"""