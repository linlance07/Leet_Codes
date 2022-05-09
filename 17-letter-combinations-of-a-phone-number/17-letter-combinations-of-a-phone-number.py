class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        D = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        for i in digits:
            ans.append(D[i])
        if len(ans)==1:
            L = []
            for j in range(len(ans[0])):
                L.append(ans[0][j])
            return L
        if len(ans)==2:
            L = []
            for k in range(len(ans[0])):
                for l in range(len(ans[1])):
                    L.append(str(ans[0][k]+ans[1][l]))
            return L
        if len(ans)==3:
            L = []
            for m in range(len(ans[0])):
                for n in range(len(ans[1])):
                    for o in range(len(ans[2])):
                        L.append(str(ans[0][m]+ans[1][n]+ans[2][o]))
            return L
        if len(ans)==4:
            L = []
            for p in range(len(ans[0])):
                for q in range(len(ans[1])):
                    for r in range(len(ans[2])):
                        for s in range(len(ans[3])):
                            L.append(str(ans[0][p]+ans[1][q]+ans[2][r]+ans[3][s]))
            return L
                    
            
        