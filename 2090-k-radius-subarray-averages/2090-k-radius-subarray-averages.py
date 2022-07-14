class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        K = k * 2 + 1
        ans = [-1] * len(nums)
        if k==0:
            return nums
        if K>len(nums):
            return ans
        ind = k
        s = 0
        for i in range(K):
            s += nums[i]
        ans[ind] = s//K
        ind += 1
        for j in range(K,len(nums)):
            s -= nums[j-K]
            s += nums[j]
            ans[ind] = s//K
            ind += 1
        return ans