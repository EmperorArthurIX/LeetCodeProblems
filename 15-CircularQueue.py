class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = -1
        self.size = k
        self.len = 0
        self.q = [-1]*k

    def enQueue(self, value: int) -> bool:
        if self.len >= self.size:
            return False
        if self.head == -1:
            self.head += 1
            self.tail += 1
            self.q[self.head] = value
            self.len += 1
            return True
        self.tail += 1
        self.tail = self.tail%self.size
        self.q[self.tail] = value
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len <= 0:
            return False
        self.head += 1
        self.head = self.head%self.size
        self.len -= 1
        return True

    def Front(self) -> int:
        if 0 < self.len <= self.size:
            return self.q[self.head]
        return -1

    def Rear(self) -> int:
        if 0 < self.len <= self.size:
            return self.q[self.tail]
        return -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()