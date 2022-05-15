class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s) + 1
        m = n
        s2 = s[::-1]
        mat = [[0 for _ in range(m)] for __ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:               
                    continue
                if s[i-1]!=s2[j-1]:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1])
                else:
                    mat[i][j] = 1 + mat[i-1][j-1]
        return mat[-1][-1]