class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = [0 for _ in range(target+1)]
        ans[0] = 1
        for i in range(target+1):
            for j in range(len(nums)):
                if i+nums[j]<len(ans):
                    ans[i+nums[j]] += ans[i]
            #print(ans)
        a = ans[-1]
        return a if a>=0 else 0