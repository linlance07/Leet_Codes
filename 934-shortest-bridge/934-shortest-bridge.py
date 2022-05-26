class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        V = set()
        mark = 'X'
        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or (r,c) in V or grid[r][c]<=0:
                return 
            V.add((r,c))
            grid[r][c] = mark
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        ans = 0
        Q = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    dfs(i,j)
                    mark = "Y"
                if grid[i][j]=='X':
                    Q.append((i,j))
        #print(Q)
        direct = [(1,0),(0,1),(-1,0),(0,-1)]
        #print(grid)
        while Q:
            n = len(Q)
            for __ in range(n):
                q = Q.pop(0)
                for _ in direct:
                    r = q[0] + _[0]
                    c = q[1] + _[1]
                    if r>=0 and r<rows and c>=0 and c<cols and grid[r][c]!='X' and grid[r][c]!='Y' and grid[r][c]==0:
                        if grid[q[0]][q[1]]=='X':
                                grid[r][c] = 1
                        else:
                            if grid[r][c]==0:
                                grid[r][c] = 1 + grid[q[0]][q[1]]
                        Q.append((r,c))
        ans = 10000000000
        #print(grid)
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]=='Y':
                    a = (x-1,y)
                    b = (x+1,y)
                    c = (x,y+1)
                    d = (x,y-1)
                    if a[0]>=0 and a[0]<rows and a[1]>=0 and a[1]<cols and grid[a[0]][a[1]]!='X' and grid[a[0]][a[1]]!='Y' and grid[a[0]][a[1]]!=0:
                        ans = min(ans,grid[a[0]][a[1]])
                    if b[0]>=0 and b[0]<rows and b[1]>=0 and b[1]<cols and grid[b[0]][b[1]]!='X' and grid[b[0]][b[1]]!='Y' and grid[b[0]][b[1]]!=0:
                        ans = min(ans,grid[b[0]][b[1]])
                    if c[0]>=0 and c[0]<rows and c[1]>=0 and c[1]<cols and grid[c[0]][c[1]]!='X' and grid[c[0]][c[1]]!='Y' and grid[c[0]][c[1]]!=0:
                        ans = min(ans,grid[c[0]][c[1]])
                    if d[0]>=0 and d[0]<rows and d[1]>=0 and d[1]<cols and grid[d[0]][d[1]]!='X' and grid[d[0]][d[1]]!='Y' and grid[d[0]][d[1]]!=0:
                        ans = min(ans,grid[d[0]][d[1]])
                    
        return ans
                    
                    
            