class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        N = 2**n-1
        for i in range(N+1):
            a = bin(i)[2:]
            b = '0'*(n-len(a)) + a
            res = []
            for j in range(len(b)):
                if b[j]=='1':
                    res.append(nums[j])
            if res not in ans:
                ans.append(res)
        return ans
                