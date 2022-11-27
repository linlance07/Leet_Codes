class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ans = [[0 for _ in range(cols)] for __ in range(rows)]
        ones_row = []
        zero_row = []
        ones_col = []
        zero_col = []
        for i in grid:
            ones_row.append(i.count(1))
            zero_row.append(i.count(0))
        for i in range(cols):
            o = z = 0
            for j in range(rows):
                if grid[j][i]:
                    o += 1
                else:
                    z += 1
            ones_col.append(o)
            zero_col.append(z)
        for i in range(rows):
            for j in range(cols):
                ans[i][j] = ones_row[i] + ones_col[j] - zero_row[i] - zero_col[j]
        return ans
                    