class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        s = 0
        T = 0
        for i in range(len(nums)):
            if i==0:
                s = 0
            else:
                s += nums[i-1]
            if i==len(nums)-1:
                T = 0
            else:
                T = total_sum - s - nums[i]
            if s==T:
                return i        
        return -1