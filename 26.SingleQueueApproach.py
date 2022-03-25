class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        size = len(self.q1)
        self.q1.append(x)
        while size > 0:
            self.q1.append(self.q1.pop(0))
            size -= 1

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not bool(self.q1)