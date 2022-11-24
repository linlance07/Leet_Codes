class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(board,r,c,ind):
            if ind==len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[ind]:
                return False
            res = 0
            temp = board[r][c]
            board[r][c] = '_/\_'
            left = dfs(board,r,c-1,ind+1)
            right = dfs(board,r,c+1,ind+1)
            up = dfs(board,r-1,c,ind+1)
            down = dfs(board,r+1,c,ind+1)
            res = res | left | right | down | up
            board[r][c] = temp
            return res
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if dfs(board,i,j,0):
                        return True 
        return False