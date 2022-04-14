class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1,n):
            for j in range(len(triangle[i])):
                a = b = 1000000
                if (i-1)>=0 and j<len(triangle[i-1]):
                    a = triangle[i-1][j]
                if (i-1)>=0 and (j-1)>=0:
                    b = triangle[i-1][j-1]
                triangle[i][j] += min(a,b)
        return min(triangle[-1])
        
        