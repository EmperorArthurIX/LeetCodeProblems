# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            mid = (lo + hi)//2
            val = guess(mid)
            if val == 0:
                return mid
            if val == -1:
                hi = mid - 1
            if val == 1:
                lo = mid + 1
        return mid