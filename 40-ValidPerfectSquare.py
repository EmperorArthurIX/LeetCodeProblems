class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if mid == num//mid and num%mid == 0:
                return True
            elif mid < num//mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return False