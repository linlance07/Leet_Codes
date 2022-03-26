class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tot = 2**n
        ans = []
        for i in range(tot):
            res = []
            a = bin(i)[2:]
            a = '0'*(n-len(a)) + a
            for j in range(len(a)):
                if a[j]=='1':
                    res.append(nums[j])
            ans.append(res)
        return ans