class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        n = len(nums1)
        m = len(nums2)
        dp = [[0 for _ in range(m)] for __ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if nums1[i]==nums2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]