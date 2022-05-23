class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for i in strs:
            a = i.count('0')
            b = i.count('1')
            for j in range(m,a-1,-1):
                for k in range(n,b-1,-1):
                    dp[j][k] = max(dp[j][k],1+dp[j-a][k-b])
        return dp[-1][-1]