class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        mat = [[0 for _ in range(n)] for __ in range(m)]
        for r in range(n):
            for c in range(m):
                mat[c][n-r-1] = box[r][c]
        n = len(box[0])
        m = len(box)
        for c in range(m):
            f = []
            for r in range(n-1,-1,-1):
                if mat[r][c]=='*':
                    f = []
                elif mat[r][c]=='.':
                    f.append(r)
                else:
                    if f:
                        a = f.pop(0)
                        mat[r][c],mat[a][c] = mat[a][c],mat[r][c]
                        f.append(r)
        return mat
                