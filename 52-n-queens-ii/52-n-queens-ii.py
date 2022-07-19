class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posd = set()
        negd = set()
        ans = []
        def dfs(r,board):
            nonlocal ans
            if r==n:
                B = ["".join(row) for row in board]
                ans.append(B)
                return
            for i in range(n):
                if i not in cols and r+i not in posd and r-i not in negd:
                    board[r][i] = 'Q'
                    cols.add(i)
                    posd.add(r+i)
                    negd.add(r-i)
                    dfs(r+1,board)
                    board[r][i] = '.'
                    cols.remove(i)
                    posd.remove(r+i)
                    negd.remove(r-i)   
        board = [['.' for __ in range(n)] for _ in range(n)]
        dfs(0,board)
        return len(ans)
                
            
            