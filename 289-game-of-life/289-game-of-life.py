class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        r = len(board)
        c = len(board[0])
        D = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)]
        mat = [[8 for _ in range(c)] for __ in range(r)]
        for i in range(r):
            for j in range(c):
                one = 0
                if board[i][j]:
                    for k in D:
                        R = i + k[0]
                        C = j + k[1]
                        if R>=0 and R<r and C>=0 and C<c:
                            if board[R][C]:
                                one += 1
                    if one<2:
                        mat[i][j] = 0
                    elif one==2 or one==3:
                        mat[i][j] = 1
                    elif one>3:
                        mat[i][j] = 0
                else:
                    for k in D:
                        R = i + k[0]
                        C = j + k[1]
                        if R>=0 and R<r and C>=0 and C<c:
                            if board[R][C]:
                                one += 1
                    if one==3:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = 0
        board[:] = mat
        