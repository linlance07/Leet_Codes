setrecursionlimit(10**5)
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.eow = False

class Solution:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        temp = self.root
        for l in word:
            if l not in temp.children:
                temp.children[l] = Node()
            temp = temp.children[l]
        temp.eow = True
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        self.n = len(words)
        for i in words:
            self.insert(i)
        ans = []
        temp = self.root
        def dfs(board,r,c,temp,path):
            nonlocal ans
            if self.n==0:
                return
            if temp.eow:
                ans.append(path)
                temp.eow = False
                self.n -= 1
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]=='X' or board[r][c] not in temp.children:
                return
            t = board[r][c]
            board[r][c] = 'X'
            dfs(board,r,c-1,temp.children[t],path+t)
            dfs(board,r,c+1,temp.children[t],path+t)
            dfs(board,r-1,c,temp.children[t],path+t)
            dfs(board,r+1,c,temp.children[t],path+t)
            board[r][c] = t
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in temp.children:
                    dfs(board,i,j,temp,"")
        return list(set(ans))