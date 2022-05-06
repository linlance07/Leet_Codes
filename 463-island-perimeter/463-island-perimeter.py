class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    count = 0
                    direct = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                    for k in range(4):
                        r = direct[k][0]
                        c = direct[k][1]
                        if r>=0 and r<rows and c>=0 and c<cols and grid[r][c]:
                            count += 1
                    ans += 4 - count
        return ans