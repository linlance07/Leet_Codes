class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        free = 1
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    r,c = i,j
                elif grid[i][j]==0:
                    free += 1
        ans = 0
        def dfs(r,c,free):
            nonlocal ans
            if r>=rows or r<0 or c<0 or c>=cols or grid[r][c]<0:
                return
            if grid[r][c]==2:
                ans += (free==0)
                return
            grid[r][c] = -3
            dfs(r-1,c,free-1)
            dfs(r,c-1,free-1)
            dfs(r+1,c,free-1)
            dfs(r,c+1,free-1)
            grid[r][c] = 0
        dfs(r,c,free)
        return ans