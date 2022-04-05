class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 0,n
        while l<=r:
            mid = (l+r)//2
            curr = (mid*(mid+1))//2
            if curr==n:
                return mid
            if n<curr:
                r = mid - 1
            else:
                l = mid + 1
        return r
            