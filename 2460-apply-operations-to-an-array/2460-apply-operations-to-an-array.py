class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        z = nums.count(0)
        ans = []
        for i in nums:
            if i:
                ans.append(i)
        return ans + [0]*z