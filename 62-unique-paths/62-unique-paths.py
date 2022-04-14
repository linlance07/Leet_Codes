class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for i in range(n)] for j in range(m)]
        rows = m
        cols = n
        for i in range(rows):
            for j in range(cols):
                if i and j:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]
                elif i:
                    mat[i][j] = mat[i-1][j]
                elif j:
                    mat[i][j] = mat[i][j-1]
                else:
                    mat[i][j] = 1
        return mat[-1][-1]
        
        