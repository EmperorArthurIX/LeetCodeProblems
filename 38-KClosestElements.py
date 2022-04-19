'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = 0
        hi = len(arr)-1
        res = []

        if hi + 1 == k:
            return arr

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] == x:
                lo = mid
                hi = mid
            elif arr[mid] < x:
                lo = mid
            elif arr[mid] > x:
                hi = mid
            if lo == hi:
                lo -= 1

        while len(res) < k:
            if hi > len(arr)-1 or (lo >= 0 and abs(x - arr[lo])<= abs(x - arr[hi])):
                res.insert(0, arr[lo])
                lo -= 1
            elif hi < len(arr):
                res.append(arr[hi])
                hi += 1

        return res