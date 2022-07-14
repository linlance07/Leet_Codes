class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        P = nums[:]
        N = nums[:]
        for i in range(1,len(nums)):
            if P[i-1]>0:
                P[i] += P[i-1]
            if N[i-1]<0:
                N[i] += N[i-1]
        p = max(P)
        n = min(N)
        s = sum(nums)
        if s-n==0:
            return p
        if s-n>p:
            return s-n
        return p