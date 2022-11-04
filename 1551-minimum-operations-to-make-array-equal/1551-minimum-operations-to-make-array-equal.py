class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n):
            a = (2*i) + 1
            d = n - a
            if d>0:
                ans += d
        return ans