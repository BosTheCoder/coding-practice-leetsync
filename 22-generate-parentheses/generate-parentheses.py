class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(curr:list[str], open: int, closed: int) -> None:
            # print(open, closed, curr)
            if not open:
                curr.extend([")"]*closed)
                ret.append("".join(curr))
                # print(f"added to ret {''.join(curr)}")

                for c in range(closed):
                    curr.pop()
                return
            
            # if theres enough open left, add a open bracket
            curr.append("(")
            dfs(curr, open-1,closed)
            curr.pop()

            if closed > open:
                curr.append(")")
                dfs(curr, open, closed-1)
                curr.pop()


        
        dfs([],n,n)

        return ret