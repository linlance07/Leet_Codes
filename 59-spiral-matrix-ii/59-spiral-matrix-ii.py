class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for __ in range(n)]
        r = 0
        c = 0
        Cr = n
        Rr = n
        Cl = -1
        Rl = 0
        right = 1
        left = 0
        up = 0
        down = 0
        for i in range(n*n):
            mat[r][c] = i+1
            if right:
                c+=1
                if c==Cr:
                    right = 0
                    down = 1
                    c-=1
                    r+=1
                    Cr-=1
            elif down:
                r+=1
                if r==Rr:
                    down = 0
                    left = 1
                    r-=1
                    c-=1
                    Rr-=1
            elif left:
                c-=1
                if c==Cl:
                    left = 0
                    up = 1
                    c+=1
                    r-=1
                    Cl+=1
            elif up:
                r-=1
                if r==Rl:
                    up = 0
                    right = 1
                    r+=1
                    c+=1
                    Rl+=1
        return mat
                