class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        M = [[0 for _ in range(cols)] for __ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                M[i][j] = mat[i][j]
        for i in range(rows):
            for j in range(1,cols):
                M[i][j] += M[i][j-1]
        for j in range(cols):
            for i in range(1,rows):
                M[i][j] += M[i-1][j]
        #print(M)
        for i in range(rows):
            for j in range(cols):
                r = i+k if (i+k)<=rows-1 else rows-1
                c = j+k if (j+k)<=cols-1 else cols-1
                rr = i+k if (i+k)<=rows-1 else rows-1
                cc = j-k-1 if (j-k-1)>=0 else None
                rrr = i-k-1 if (i-k-1)>=0 else None
                ccc = j+k if (j+k)<=cols-1 else cols-1
                rrrr = i-k-1 if (i-k-1)>=0 else None
                cccc = j-k-1 if (j-k-1)>=0 else None
                A = M[r][c]
                B = M[rr][cc] if (rr!=None and cc!=None) else 0
                C = M[rrr][ccc] if (rrr!=None and ccc!=None) else 0
                D = M[rrrr][cccc] if (rrrr!=None and cccc!=None) else 0
                #print(i,j,A,B,C,D,'---',r,c,rr,cc,rrr,ccc,rrrr,cccc)
                mat[i][j] = A - B - C + D
        return mat
                