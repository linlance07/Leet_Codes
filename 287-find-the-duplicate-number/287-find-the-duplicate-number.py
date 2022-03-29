class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[nums[i]%n] += n
        for j in range(n):
            if nums[j]//n>1:
                return j
        