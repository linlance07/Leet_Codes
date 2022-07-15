class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = M = m = nums[0]
        for i in range(1,len(nums)):
            L = [M*nums[i],m*nums[i],nums[i]]
            M = max(L)
            m = min(L)
            ans = max(ans,M)
        return ans
        