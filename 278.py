# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1 
        high = n
        while low < high:
            mid = (low + high)//2
            bad_version = isBadVersion(mid)
            if bad_version:
                high = mid
            else:
                low = mid+1
        return low
        