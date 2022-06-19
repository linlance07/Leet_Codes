class Solution:
    def findLHS(self, nums: List[int]) -> int:
        D = Counter(nums)
        ans = 0
        for i in D:
            if i-1 in D:
                ans = max(ans,D[i]+D[i-1])
        return ans