class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        right = x // 3 + 1
        left = 1
        while left <= right:
            mid = (left + right)//2
            if(mid*mid==x):
                return mid
        
            if(mid*mid<x):
                left=mid+1
        
            else:
                right=mid-1
        return right