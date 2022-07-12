class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        dp = [[0 for _ in range(m)] for __ in range(n)]
        for i in range(n):
            dp[i][0] = i
        for i in range(m):
            dp[0][i] = i       
        for r in range(1,n):
            for c in range(1,m):
                if word1[r-1]==word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c-1],dp[r][c-1],dp[r-1][c])
        return dp[-1][-1]
            