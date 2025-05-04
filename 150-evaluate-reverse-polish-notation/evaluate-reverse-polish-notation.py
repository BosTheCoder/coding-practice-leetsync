class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token.isnumeric() or token[1:].isnumeric():
                stack.append(int(token))
            else:
                val2, val1 = stack.pop(),stack.pop()
                match token:
                    case "+":
                        stack.append(val1 + val2)
                    case "-":
                        stack.append(val1 - val2)
                    case "*":
                        stack.append(val1 * val2)
                    case "/":
                        stack.append(int(val1 / val2))
        return stack[0]
