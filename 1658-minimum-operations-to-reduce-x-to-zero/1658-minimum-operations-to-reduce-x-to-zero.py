class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        t = sum(nums) - x
        l = 0
        s = 0
        ans = (0,0)
        for r in range(len(nums)):
            s += nums[r]
            while l<=r and s>t:
                s -= nums[l]
                l += 1
            if s==t:
                ans = (1,max(r-l+1,ans[1]))
        if ans[0]:
            return len(nums) - ans[1]
        return -1
                
            