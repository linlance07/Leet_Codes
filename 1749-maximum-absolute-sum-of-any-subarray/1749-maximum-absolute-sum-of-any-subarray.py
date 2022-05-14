class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        arr = nums.copy()
        arr2 = nums.copy()
        for i in range(1,len(nums)):
            if arr[i-1]>=0:
                arr[i] += arr[i-1]
            if arr2[i-1]<=0:
                arr2[i] += arr2[i-1]
        return max(max(arr),abs(min(arr2)))