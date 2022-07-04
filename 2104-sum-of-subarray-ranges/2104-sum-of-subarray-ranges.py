class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            l = r = nums[i]
            for j in range(i,len(nums)):
                l = min(l,nums[j])
                r = max(r,nums[j])
                ans += r - l
        return ans