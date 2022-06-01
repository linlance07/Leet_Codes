class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = mini = ans = nums[0]
        for i in range(1,len(nums)):
            L = [nums[i],nums[i]*maxi,nums[i]*mini]
            maxi = max(L)
            mini = min(L)
            ans = max(ans,maxi)
        return ans