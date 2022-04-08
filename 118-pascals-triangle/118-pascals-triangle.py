class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n==1:
            return[[1]]
        if n==2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(n-2):
            A = []
            for j in range(len(ans[-1])-1):
                A.append(ans[-1][j]+ans[-1][j+1])
            A = [1] + A + [1]
            ans.append(A)
        return ans