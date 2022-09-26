class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        ans = 0
        c = 0
        for i in nums:
            if i==maxi:
                c += 1
            else:
                c = 0
            ans = max(ans,c)
        return ans
            
            
            
            