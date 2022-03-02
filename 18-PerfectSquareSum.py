# THIS IS A LITERAL DP SOLUTION.
"""
When debugged, we see a pattern. `dp[i]` contains the minimum number of additions to be performed, of numbers within `squares`, to get `i`

All indices that are direct multiples of a square carry the value of the coefficient

All other indices carry the count of squares which add up to the index

Minimum number is ensured by the condition `dp[j] = min(dp[j], dp[j-s] + 1)` which just so happens to be the relation between these square-sum combinations

Of course, we require only the final index, `n`, so we return `dp[n]`

However, this can actually be used to find the combinations for all numbers up to `n`
"""
import math
inf = 1e4 + 1
def numSquares(n: int) -> int:
    
    squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
    return ways(squares, n)

def ways(squares, n):
    dp = [inf]*(n+1)
    dp[0] = 0
    for s in squares:
        for j in range(s,n+1):
            if dp[j-s] is not inf:
                dp[j] = min(dp[j], dp[j-s] + 1)
    return dp[n]

if __name__ == "__main__":
    print(numSquares(29))