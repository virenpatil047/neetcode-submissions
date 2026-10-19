class MinStack:

    def __init__(self):
        self.minStack = []
        self.m = None

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.m == None or val < self.m:
            self.m = val

    def find_new_min(self):
        m = None
        if self.minStack:
            m = self.minStack[0]
            for v in self.minStack:
                if v < m:
                    m = v
        self.m = m

    def pop(self) -> None:
        if self.m == self.minStack.pop():
            self.find_new_min()
    
    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.m