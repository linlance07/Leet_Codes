class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        D = {}
        for i in matches:
            a,b = i
            if a not in D:
                D[a] = [0,0]
            if b not in D:
                D[b] = [0,0]
            D[a][0] = 1
            D[b][1] += 1
        win = []
        lose = []
        ans = []
        for j in D:
            l = D[j][1]
            if l==0:
                win.append(j)
            elif l==1:
                lose.append(j)
        ans.append(sorted(win))
        ans.append(sorted(lose))
        return ans