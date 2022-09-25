class MyCircularQueue:
    def __init__(self, k: int):
        self.Q = deque()
        self.n = k
    def enQueue(self, value: int) -> bool:
        if len(self.Q)<self.n:
            self.Q.append(value)
            return True
        return False
    def deQueue(self) -> bool:
        if len(self.Q)!=0:
            self.Q.popleft()
            return True
        return False
    def Front(self) -> int:
        if self.Q:
            return self.Q[0]
        return -1       
    def Rear(self) -> int:
        if self.Q:
            return self.Q[-1]
        return -1
    def isEmpty(self) -> bool:
        if self.Q:
            return False
        return True
    def isFull(self) -> bool:
        if len(self.Q)==self.n:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()