class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s)+1)
        memo[-1] = True
        hash = set(wordDict)
        for i in range(len(s)-1,-1,-1):
            for val in hash:
                # print(i, s[i:i+len(val)], val)
                if s[i:i+len(val)] == val and memo[len(val) + i]:
                    # print("foud")
                    memo[i] = True
        print(memo)
        return memo[0]
        