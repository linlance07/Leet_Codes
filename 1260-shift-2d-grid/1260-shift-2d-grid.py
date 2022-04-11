class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        mat = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                a = (j+k)%c
                b = (j+k)//c
                mat[(i+b)%r][a] = grid[i][j]
        return mat