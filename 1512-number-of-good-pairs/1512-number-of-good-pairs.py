class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        D = defaultdict(lambda:0)
        ans = 0
        for i in nums:
            ans += D[i]
            D[i] += 1
        return ans