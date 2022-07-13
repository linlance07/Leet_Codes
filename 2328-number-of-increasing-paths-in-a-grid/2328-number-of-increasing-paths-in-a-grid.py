class Solution:
    def countPaths(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        dp = [[0 for _ in range(m)] for __ in range(n)]
        def dfs(r,c,p):
            if r<0 or r>=n or c<0 or c>=m or mat[r][c]<=p:
                return 0
            if dp[r][c]!=0:
                return dp[r][c]
            dp[r][c] = 1
            left = dfs(r,c-1,mat[r][c])
            right = dfs(r,c+1,mat[r][c])
            up = dfs(r-1,c,mat[r][c])
            down = dfs(r+1,c,mat[r][c])
            dp[r][c] = (dp[r][c] + left + right + up + down) % (10**9+7)
            return dp[r][c]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = (ans + dfs(i,j,-1)) % (10**9+7)
        return ans