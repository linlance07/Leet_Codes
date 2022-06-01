class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i]<0 or nums[i]>=n:
                nums[i] = 0
        for j in range(n):
            nums[nums[j]%n] += n
        for k in range(n):
            if nums[k]//n==0:
                return k
        return n