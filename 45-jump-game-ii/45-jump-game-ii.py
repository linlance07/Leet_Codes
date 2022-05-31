class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        l = 0
        r = nums[0]
        ans = 1
        while r<len(nums)-1:
            #print(l,r)
            nxt = max([j+nums[j] for j in range(l,r+1)])
            l,r = r,nxt
            ans += 1
        return ans