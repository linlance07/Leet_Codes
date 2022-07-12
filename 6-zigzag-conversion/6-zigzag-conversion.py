class Solution:
    def convert(self, s: str, numRows: int) -> str:
        D = [(1,1),(-1,1)]
        line = [["" for _ in range(1001)] for __ in range(numRows)]
        j = 0
        r,c = (0,0)
        for i in s:
            #print(r,c)
            line[r][c] = i
            r = r + D[j][0]
            c = c + D[j][1]
            if r>=numRows or r<0:
                r -= D[j][0]
                j = (j+1)%2
                r += D[j][0]
        ans = ""
        for k in line:
            ans += "".join(k)
        return ans
            
            