class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
        D = {}
        ans = (0,0,0)
        l = 0
        for r in range(len(nums)):
            if nums[r] in D and D[nums[r]]>=l:
                l = D[nums[r]] + 1
            D[nums[r]] = r
            if l==0:
                if pre[r]>ans[2]:
                    ans = (l,r,pre[r])
            else:
                if pre[r]-pre[l-1]>ans[2]:
                    ans = (l,r,pre[r]-pre[l-1])
        
        return ans[2]