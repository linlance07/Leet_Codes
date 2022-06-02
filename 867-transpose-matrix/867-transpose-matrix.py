class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        mat = []
        for i in range(cols):
            res = []
            for j in range(rows):
                res.append(matrix[j][i])
            mat.append(res)
        return mat