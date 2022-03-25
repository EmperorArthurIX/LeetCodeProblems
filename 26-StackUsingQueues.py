class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())
            return self.q2.pop(0)
        return self.q2.pop(0)

    def top(self) -> int:
        if self.q1:
            return self.q1[-1]
        if self.q2:
            return self.q2[0]
    def empty(self) -> bool:
        return not bool(self.q1 or self.q2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()