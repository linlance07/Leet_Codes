class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        ans = 0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid2[r][c]==0:
                return
            grid2[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] and grid1[i][j]==0:
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]:
                    dfs(i,j)
                    ans += 1
        return ans
                    
                    