class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        already = set()
        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in already:
                return 0
            already.add((r,c))
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    ans = max(ans,dfs(i,j))
        return ans