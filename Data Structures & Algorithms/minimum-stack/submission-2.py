class MinStack:

    def __init__(self):
        self.minStack = []
        self.m = float('inf')

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(0)
            self.m = val
        else:
            self.minStack.append(val - self.m)
            if val < self.m:
                self.m = val

    def pop(self) -> None:
        if not self.minStack:
            return
        p = self.minStack.pop()
        if p < 0:
            self.m = self.m - p
    
    def top(self) -> int:
        if not self.minStack:
            return
        if self.minStack[-1] < 0:
            return self.m
        return self.m + self.minStack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return
        return self.m