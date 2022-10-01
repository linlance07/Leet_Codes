class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans += [nums[i]]
        return ans