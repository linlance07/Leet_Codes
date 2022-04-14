class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mat = obstacleGrid
        rows = len(mat)
        cols = len(mat[0])
        if mat[0][0] or mat[-1][-1]:
            return 0
        for i in range(rows):
            for j in range(cols):
                if i and j:
                    if mat[i][j]:
                        mat[i][j] = 0
                    else:
                        mat[i][j] = mat[i-1][j] + mat[i][j-1]
                elif i:
                    if mat[i][j]:
                        mat[i][j] = 0
                    else:
                        mat[i][j] = mat[i-1][j]
                elif j:
                    if mat[i][j]:
                        mat[i][j] = 0
                    else:
                        mat[i][j] = mat[i][j-1]                    
                else:
                    mat[i][j] = 1
        return mat[-1][-1]
                    