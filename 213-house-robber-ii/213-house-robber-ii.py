class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        first = nums[0:N-1]
        second = nums[1:N]
        def finder(arr):
            if len(arr)<=2:
                return max(nums)
            dp = []
            dp.append(arr[0])
            dp.append(max(arr[:2]))
            for j in range(2,len(arr)):
                dp.append(max(dp[-1],dp[-2]+arr[j]))
            return dp[-1]
        a = finder(first)
        b = finder(second)
        return max(a,b)