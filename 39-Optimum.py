class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(n)
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)

        half_sol = self.myPow(x, n//2)
        if n % 2 == 0:
            return half_sol * half_sol
        else:
            return half_sol * half_sol * x


if __name__ == '__main__':
    print(Solution().myPow(2,10))