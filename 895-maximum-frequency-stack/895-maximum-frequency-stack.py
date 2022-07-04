class FreqStack:

    def __init__(self):
        self.stack = [[] for _ in range(20000)]
        self.last = 0
        self.D = defaultdict(int)

    def push(self, val: int) -> None:
        if val in self.D:
            self.D[val] += 1
        else:
            self.D[val] = 0
        self.stack[self.D[val]].append(val)
        self.last = max(self.last,self.D[val])
        #print(self.stack)
        
    def pop(self) -> int:
        if not self.stack[self.last]:
            return -1
        x = self.stack[self.last].pop()
        if not self.stack[self.last]:
            self.last -= 1
        self.D[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()