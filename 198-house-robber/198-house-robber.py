class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[:2]))
        for i in range(2,len(nums)):
            dp.append(max(dp[-1],dp[-2]+nums[i]))
        print(dp)
        return dp[-1]