class Solution:
    def numTrees(self, n: int) -> int:
        a = b = c = 1
        for i in range(1,2*n+1):
            a *= i
        for j in range(1,n+1):
            b *= j
        for k in range(1,n+2):
            c *= k
        return a//(b*c)
        