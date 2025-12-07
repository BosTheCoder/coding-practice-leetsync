class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, val: int) -> None:
        self.stack.append(
            (val, self.mini)
        )
        self.mini = min(self.mini,val) if self.mini is not None else val
        

    def pop(self) -> None:
        val, mini = self.stack.pop()
        self.mini = mini
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()