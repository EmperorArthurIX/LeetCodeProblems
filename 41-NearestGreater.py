import bisect

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

class Solution2():
    def nextGreatestLetter(self, letters, target):
        lo = 0
        hi = len(letters)
        while (lo < hi):
            mid = lo + (hi - lo) // 2
            if (letters[mid] <= target):
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]