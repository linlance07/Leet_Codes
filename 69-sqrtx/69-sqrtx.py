class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l = 0
        r = x//2
        while l<=r:
            mid = (l+r)//2
            if mid**2==x:
                return mid
            if mid**2<x:
                l = mid + 1
            else:
                r = mid - 1
        return r