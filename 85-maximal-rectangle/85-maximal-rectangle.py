class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        ans = 0
        row = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row[j] = row[j]+1 if mat[i][j]=='1' else 0
            stack = []
            for k,h in enumerate(row+[0]):
                while stack and stack[-1][1]>=h:
                    H = stack.pop()[1]
                    W = k if not stack else k-stack[-1][0]-1
                    ans = max(ans,H*W)
                stack.append((k,h))
        return ans
                