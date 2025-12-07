class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(open, close, arr):
            if close > open:
                return 
            if open == n and close == n:
                ret.append("".join(arr))
                return
            if open + close > 2 * n:
                return 
                
            # add open bracket
            arr.append("(")
            dfs(open+1,close,arr)
            arr.pop()

            # Add close bracket
            arr.append(")")
            dfs(open, close+1, arr)
            arr.pop()


        dfs(0,0,[])
        return ret