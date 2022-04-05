class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi,mini,ans = [nums[0]]*3
        for i in range(1,len(nums)):
            lis = [nums[i],nums[i]*maxi,nums[i]*mini]
            maxi = max(lis)
            mini = min(lis)
            ans = max(ans,maxi)
        return ans