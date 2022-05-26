class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mat = [0 for __ in range(n)]
        D = {}
        for i in range(len(trust)):
            r = trust[i][0]
            mat[r-1] = 1
            D[trust[i][1]] = D.get(trust[i][1],0)+1
        for j in range(len(mat)):
            if mat[j]:
                continue
            else:
                if D.get(j+1,0)==n-1:
                    return j+1
        return -1