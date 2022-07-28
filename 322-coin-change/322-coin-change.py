class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp = [0]*(amount+1)
        for i in range(amount+1):
            for j in coins:
                if i+j<amount+1 and (i==0 or dp[i]):
                    if dp[i+j]:
                        dp[i+j] = min(dp[i+j],dp[i]+1)
                    else:
                        dp[i+j] = dp[i] + 1
        return dp[-1] if dp[-1] else -1
        
        