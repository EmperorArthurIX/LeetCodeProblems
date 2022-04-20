class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n%2 == 0 and x < 0:
            x = abs(x)
        if n < 0:
            n = -n
            return self.myPow(1/x, n)
        if n%2 == 0:
            l = self.myPow(x, n//2)
            return l*l
        else:
            l = self.myPow(x, n//2)
            return l*l*x