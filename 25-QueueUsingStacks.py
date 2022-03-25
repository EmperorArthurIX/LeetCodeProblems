class MyQueue:

    def __init__(self):
        self.size = 0
        self.stack = []
        self.q = []

    def push(self, x: int) -> None:
        if len(self.q) == 0:
            self.stack.append(x)
        else:
            while len(self.q):
                self.stack.append(self.q.pop())
            self.stack.append(x)
        while len(self.stack):
            self.q.append(self.stack.pop())
        self.size += 1
    
    def pop(self) -> int:
        self.size -= 1
        val = self.q[-1]
        del self.q[-1]
        return val

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if self.size == 0:
            return True
        else: return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()