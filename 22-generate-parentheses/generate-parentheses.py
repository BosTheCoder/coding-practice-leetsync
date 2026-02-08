class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def generate(open: int, closed: int, arr: list[str]):
            if open==n and closed == n:
                ret.append("".join(arr))
                return

            if open < n:
                arr.append("(")
                open += 1
                generate(open,closed, arr)
                arr.pop()
                open -= 1


            if closed < open:
                arr.append(")")
                closed += 1
                generate(open, closed, arr)
                arr.pop()
                closed -= 1

        generate(0,0,[])
        return ret