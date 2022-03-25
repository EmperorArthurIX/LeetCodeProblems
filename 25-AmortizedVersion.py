class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        while self.s1:
            val = self.s1[0]
            del self.s1[0]
            self.s2.append(self.s1.pop())
            return val
    def peek(self) -> int:
        return self.s1[0]
    def empty(self) -> bool:
        return not bool(self.s1 or self.s2)