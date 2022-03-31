class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        l = 0
        r = 0
        prod = 1
        while r<len(nums):
            prod = prod * nums[r]
            while prod>=k:
                prod = prod//nums[l]
                l += 1
            ans += r - l + 1
            r += 1
        return ans