class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for j in range(1,len(nums)):
            nums[j] += nums[j-1]
        return nums