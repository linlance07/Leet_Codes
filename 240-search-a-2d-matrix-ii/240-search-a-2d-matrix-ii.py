class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(cols):
            if matrix[rows-1][i]==target:
                return True
            if matrix[rows-1][i]>target:
                j = 0
                k = rows-1
                while j<=k:
                    mid = (j+k)//2
                    if matrix[mid][i]==target:
                        return True
                    if matrix[mid][i]<target:
                        j = mid+1
                    else:
                        k = mid-1
        return False
        