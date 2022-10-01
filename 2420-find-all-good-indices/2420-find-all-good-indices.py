class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        pre = [1]*len(nums)
        suf = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                pre[i] = pre[i-1] + 1
        for j in range(len(nums)-2,-1,-1):
            if nums[j]<=nums[j+1]:
                suf[j] = suf[j+1] + 1
        ans = []
        # print(pre)
        # print(suf)
        for i in range(k,len(nums)-k):
            if pre[i-1]>=k and suf[i+1]>=k:
                ans.append(i)
        return ans
                       
            