class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        a = n // 3
        n -= (a*3)
        b = n // 2
        n -= (b*2)
        if n:
            b += 2
            a -= 1
        return (3**a) * (2**b)
            