class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "/", "*"}
        for token in tokens:
            if token not in ops:
                # print("found number", token)
                stack.append(int(token))
                continue
            
            # print("this is the stack before popping",stack, token)
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "*":
                stack.append(a*b)
            else:
                val = a/b
                val = math.floor(val) if val >= 0 else math.ceil(val)
                stack.append(val)
        return stack[0]
