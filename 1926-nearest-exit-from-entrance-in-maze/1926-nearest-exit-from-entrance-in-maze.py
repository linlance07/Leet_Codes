class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        borders = []
        for i in range(rows):
            if [i,0]!=entrance: 
                if maze[i][0]=='.':
                    borders.append((i,0))
                    maze[i][0] = 0
            if [i,cols-1]!=entrance:
                if maze[i][-1]=='.':
                    borders.append((i,cols-1))
                    maze[i][-1] = 0
        for i in range(cols):
            if [0,i]!=entrance: 
                if maze[0][i]=='.':
                    borders.append((0,i))
                    maze[0][i] = 0
            if [rows-1,i]!=entrance:
                if maze[-1][i]=='.':
                    borders.append((rows-1,i))
                    maze[-1][i] = 0
        direct = [(1,0),(0,1),(-1,0),(0,-1)]
        print(borders)
        while borders:
            n = len(borders)
            for _ in range(n):
                q = borders.pop(0)
                for d in direct:
                    r = d[0] + q[0]
                    c = d[1] + q[1]
                    if r>=0 and r<rows and c>=0 and c<cols and maze[r][c]=='.':
                        if r==entrance[0] and c==entrance[1]:
                            if maze[r][c]=='.':
                                maze[r][c] = 1 + maze[q[0]][q[1]]
                            else:
                                maze[r][c] = min(maze[r][c],1 + maze[q[0]][q[1]])
                        else:
                            maze[r][c] = 1 + maze[q[0]][q[1]]
                        borders.append((r,c))
        print(maze)
        if maze[entrance[0]][entrance[1]]=='.':
            return -1
        return maze[entrance[0]][entrance[1]]
            
            
        