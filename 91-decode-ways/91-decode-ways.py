class Solution:
    def numDecodings(self, s: str) -> int:
        if s=='' or s[0]=='0':
            return 0
        dp = [1]*len(s)
        for i in range(1,len(s)):
            if int(s[i]):
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            if 10<=int(s[i-1:i+1])<=26:
                dp[i] += dp[i-2 if i>=2 else 0]
        return dp[-1]
                    
        