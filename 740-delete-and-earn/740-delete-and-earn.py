class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        D = Counter(nums)
        nums = sorted(set(nums))
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0] * D[nums[0]]
        for i in range(1,len(nums)):
            p = nums[i] * D[nums[i]]
            if nums[i]-nums[i-1]==1:
                dp[i+1] = max(dp[i],p+dp[i-1])
            else:
                dp[i+1] = p + dp[i]
        return dp[-1]