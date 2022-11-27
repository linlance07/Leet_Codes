class Solution:
    def pivotInteger(self, n: int) -> int:
        r = (n*(n+1))//2
        l = 0
        for i in range(1,n+1):
            l += i
            r -= i-1
            if l==r:
                return i
        return -1