class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        Q = []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    Q.append((i,j)) 
                else:
                    mat[i][j] = -1
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        while len(Q):
            q = Q.pop(0)
            for i in dir:
                r = q[0]+i[0]
                c = q[1]+i[1]
                if r<0 or r==rows or c<0 or c==cols:
                    continue
                if mat[r][c]==-1:
                    mat[r][c] = mat[q[0]][q[1]] + 1
                    Q.append((r,c))                    
        return mat
            