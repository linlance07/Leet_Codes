class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) + 1
        m = len(text2) + 1
        mat = [[0 for _ in range(m)] for __ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:               
                    continue
                if text1[i-1]!=text2[j-1]:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1])
                else:
                    mat[i][j] = 1 + mat[i-1][j-1]
        return mat[-1][-1]