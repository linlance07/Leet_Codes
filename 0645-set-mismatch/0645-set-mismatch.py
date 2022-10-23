class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        D = [0]*len(nums)
        ans = []
        for i in range(len(nums)):
            if D[nums[i]-1]!=0:
                ans.append(nums[i])
            else:
                D[nums[i]-1] = 1
        ans.append(D.index(0)+1)
        return ans
        