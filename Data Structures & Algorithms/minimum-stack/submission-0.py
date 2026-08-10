class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_value=self.stack[0]
        for x in self.stack:
            if x<min_value:
                min_value=x
        return min_value
        
