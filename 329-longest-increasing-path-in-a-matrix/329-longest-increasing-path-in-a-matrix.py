class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        dp = [[-1 for _ in range(m)] for __ in range(n)]
        def dfs(r,c,p):
            if r<0 or r>=n or c<0 or c>=m or mat[r][c]<=p:
                return 0
            if dp[r][c]!=-1:
                return dp[r][c]
            left = dfs(r,c-1,mat[r][c])
            right = dfs(r,c+1,mat[r][c])
            up = dfs(r-1,c,mat[r][c])
            down = dfs(r+1,c,mat[r][c])
            dp[r][c] = 1 + max(left,right,up,down)
            return dp[r][c]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans,dfs(i,j,-1))
        return ans
                