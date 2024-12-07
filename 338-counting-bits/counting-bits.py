class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1s(s: str)->int:
            count = 0
            for c in s:
                if c == "1":
                    count+=1
            return count
        ret = [0] * (n+1)
        for i in range(n+1):
            ret[i]=count1s(f"{i:b}")
        return ret