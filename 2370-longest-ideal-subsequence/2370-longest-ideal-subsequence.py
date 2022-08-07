class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for i in s:
            x = ord(i)
            dp[x] = max(dp[x-k:x+k+1]) + 1
        return max(dp)