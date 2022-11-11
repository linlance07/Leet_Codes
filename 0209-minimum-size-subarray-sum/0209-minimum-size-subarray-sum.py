class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        l = 0
        r = 0
        ans = None
        while r<len(nums):
            s += nums[r]
            #print(s)
            while s>=target:
                if ans==None:
                    ans = r - l + 1
                else:
                    ans = min(ans,r-l+1)
                s -= nums[l]
                l += 1
            r += 1
        return 0 if ans==None else ans
            