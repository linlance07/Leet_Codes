class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        Q = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    Q.append((i,j))
        Dir = [(0,1),(0,-1),(1,0),(-1,0)]
        while Q:
            n = len(Q)
            for _ in range(n):
                q = Q.pop(0)
                for x in Dir:
                    r = q[0] + x[0]
                    c = q[1] + x[1]
                    if r>=0 and r<rows and c>=0 and c<cols and grid[r][c]==0:
                        grid[r][c] = 1 + grid[q[0]][q[1]]
                        Q.append((r,c))
        maxi = 0
        for k in grid:
            maxi =  max(maxi,max(k))
        if maxi==1:
            return -1
        return maxi - 1
                    