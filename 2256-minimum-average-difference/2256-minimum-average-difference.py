class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans = (float('inf'),0)
        b = sum(nums)
        a = 0
        for i in range(len(nums)):
            a += nums[i]
            b -= nums[i]
            A = int(a/(i+1))
            if i==len(nums)-1:
                B = 0
            else:
                B = int(b/(len(nums)-i-1))
            c = abs(A-B)
            if c<ans[0]:
                ans = (c,i)
        return ans[1]
            