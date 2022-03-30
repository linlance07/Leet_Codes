class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        for i in range(len(self.mat)):
            for j in range(1,len(self.mat[0])):
                self.mat[i][j] += self.mat[i][j-1]
        for i in range(len(self.mat[0])):
            for j in range(1,len(self.mat)):
                self.mat[j][i] += self.mat[j-1][i]
        '''for _ in self.mat:
            print(*_)'''
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tot_sum = self.mat[row2][col2]
        a = b = c = 0
        if col1-1>=0:
            a = self.mat[row2][col1-1]
        if row1-1>=0:
            b = self.mat[row1-1][col2]
        if row1-1>=0 and col1-1>=0:
            c = self.mat[row1-1][col1-1]
        #print(tot_sum,a,b,c)
        return tot_sum - a - b + c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)