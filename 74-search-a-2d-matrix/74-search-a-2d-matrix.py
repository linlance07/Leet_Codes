class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if matrix[i][-1]>target:
                l = 0
                r = cols-1
                while l<=r:
                    mid = (l+r)//2
                    if matrix[i][mid]>target:
                        r = mid-1
                    elif matrix[i][mid]<target:
                        l = mid+1
                    else:
                        return True
            elif matrix[i][-1]==target:
                return True
        return False
            