class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        l = 0
        r = nums[0]
        ans = 1
        while r<len(nums)-1:
            maxi = 0
            for j in range(l,r+1):
                maxi = max(maxi,j + nums[j])
            l = r
            r = maxi
            ans += 1
        return ans