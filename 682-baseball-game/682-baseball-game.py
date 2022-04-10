class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for i in range(len(ops)):
            if ops[i] == 'C':
                ans.pop()
            elif ops[i] == 'D':
                ans.append(ans[len(ans)-1]*2)
            elif ops[i] == '+':
                ans.append(ans[len(ans)-1]+ans[len(ans)-2])
            else:
                ans.append(int(ops[i]))
        return sum(ans)
        