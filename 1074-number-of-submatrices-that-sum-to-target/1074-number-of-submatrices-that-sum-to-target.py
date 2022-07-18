class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(1,cols):
                mat[i][j] += mat[i][j-1]
        ans = 0
        for i in range(cols):
            for j in range(i,cols):
                D = defaultdict(int)
                D[0] = 1
                s = 0
                for k in range(rows):
                    if i>0:
                        s += mat[k][j] - mat[k][i-1]
                    else:
                        s += mat[k][j]
                    ans += D[s-target]
                    D[s] += 1
        return ans