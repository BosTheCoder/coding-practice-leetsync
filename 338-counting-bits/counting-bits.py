class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0 = 0
        01 = 1
        10 = 2
        11 =

        """
        nums = [0] * (n+1)
        for i in range(n+1):
            s = str(bin(i))[2:]
            num_ones = len([c for c in s if c == "1"])
            nums[i] = num_ones
        return nums


"""
0 0
1 1
2 10
3 11
4 100
5 101
6 110
7 111
8 1000
9 1001


"""