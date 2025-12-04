class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(arr:list, open:int):
            # print(arr, open, len(arr), n* 2)
            if len(arr) == n * 2:
                if open == 0:
                    ret.append("".join(arr))
                return
            
            if open < n:
                # we can still add open brackets
                arr.append("(")
                open += 1
                dfs(arr, open)
                open-=1
                arr.pop()
            if open>0:
                arr.append(")")
                open -= 1
                dfs(arr, open)
                open += 1
                arr.pop()


        dfs([],0)

        return ret