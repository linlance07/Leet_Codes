class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        ans = 0
        for i in S:
            if i-1 in S:
                continue
            x = 1
            while i+x in S:
                x += 1
            ans = max(ans,x)
        return ans