class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or grid[r][c]:
                return
            grid[r][c] = 1
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)          
        ans = 0
        for i in range(rows):
            if grid[i][0]==0:
                dfs(i,0)
            if grid[i][-1]==0:
                dfs(i,cols-1)
        for i in range(cols):
            if grid[0][i]==0:
                dfs(0,i)
            if grid[-1][i]==0:
                dfs(rows-1,i)
        for j in range(1,rows-1):
            for k in range(1,cols-1):
                if grid[j][k]==0:
                    ans += 1
                    dfs(j,k)
        return ans