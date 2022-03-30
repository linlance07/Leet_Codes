class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        ans = [-1]*n
        stack = []
        for i in range(len(nums)+len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            if stack:
                ans[i%n] = stack[-1]
            stack.append(nums[i%n])
        return ans