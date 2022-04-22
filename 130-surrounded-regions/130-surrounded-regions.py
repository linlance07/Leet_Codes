class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]=='X' or board[r][c]=='A':
                return 
            board[r][c] = 'A'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for i in range(cols):
            if board[0][i]=='O':
                dfs(0,i)
            if board[-1][i]=='O':
                dfs(rows-1,i)
        for j in range(rows):
            if board[j][0]=='O':
                dfs(j,0)
            if board[j][-1]=='O':
                dfs(j,cols-1)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j]=='A':
                    board[i][j] = 'O'
        
            
            
            
        