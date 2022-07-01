class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        ans = 0
        for i in nums:
            ans += abs(i-med)
        return ans