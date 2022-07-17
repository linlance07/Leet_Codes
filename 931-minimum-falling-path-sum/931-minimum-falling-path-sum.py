class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(1,rows):
            for j in range(cols):
                a = b = c = 1000000
                if (i-1)>=0 and (j-1)>=0:
                    a = matrix[i-1][j-1]
                if (i-1)>=0 and j>=0:
                    b = matrix[i-1][j]
                if (i-1)>=0 and (j+1)<cols:
                    c = matrix[i-1][j+1]
                matrix[i][j] += min(a,b,c)
        return min(matrix[-1])
            