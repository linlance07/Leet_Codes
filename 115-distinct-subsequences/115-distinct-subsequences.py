class Solution:
    def numDistinct(self, A: str, B: str) -> int:
        n = len(A) + 1
        m = len(B) + 1
        dp = [[1 for _ in range(m)] for __ in range(n)]
        for i in range(1,m):
            dp[0][i] = 0
        for r in range(1,n):
            for c in range(1,m):
                if A[r-1]==B[c-1]:
                    dp[r][c] = dp[r-1][c] + dp[r-1][c-1]
                else:
                    dp[r][c] = dp[r-1][c]
        return dp[-1][-1]