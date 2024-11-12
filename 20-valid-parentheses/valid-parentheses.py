class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c not in brackets:
                stack.append(c)
                continue
            
            opp = brackets[c]
            if stack and stack[-1] == opp:
                stack.pop()
            else:
                return False
        return len(stack) == 0