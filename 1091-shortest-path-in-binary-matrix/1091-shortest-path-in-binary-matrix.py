class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])     
        if grid[0][0] or grid[rows-1][cols-1]:
            return -1
        Q = [(0,0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    grid[i][j] = '#'
                else:
                    grid[i][j] = 'O'
        dir = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        '''for x in range(rows):
            print(*grid[x])'''
        grid[0][0] = 1
        while len(Q):
            q = Q.pop(0)
            for i in dir:
                r = q[0] + i[0]
                c = q[1] + i[1]
                if r<0 or r==rows or c<0 or c==cols or grid[r][c]=='#':
                    continue
                if grid[r][c]=='O':
                    grid[r][c] = 1 + grid[q[0]][q[1]]
                    Q.append((r,c))
                    #print(q,i,r,c,grid[r][c])
        #print(grid)
        if grid[-1][-1]=='O':
            return -1
        return grid[-1][-1]