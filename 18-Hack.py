# NOW THERE IS BIT-MANIPULATION? HOW?

import math

def isSquare(self, n: int) -> bool:
    sq = int(math.sqrt(n))
    return sq*sq == n

def numSquares(self, n: int) -> int:
    # four-square and three-square theorems
    while (n & 3) == 0:
        n >>= 2      # reducing the 4^k factor from number
    if (n & 7) == 7: # mod 8
        return 4

    if isSquare(n):
        return 1
    # check if the number can be decomposed into sum of two squares
    for i in range(1, int(n**(0.5)) + 1):
        if isSquare(n - i*i):
            return 2
    # bottom case from the three-square theorem
    return 3
    # dp = [i for i in range(n+1)]
    # for num in range(n+1):
    #     curr = 0
    #     delta = 0
    #     while delta <= num:
    #         dp[num] = min(dp[num-delta]+1, dp[num])
    #         delta += (2*curr+1)
    #         curr += 1
    # return dp[num]


if __name__ == "__main__":
    print(numSquares(29))