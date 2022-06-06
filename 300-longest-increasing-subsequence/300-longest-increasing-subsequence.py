class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]<i:
                    stack.append(i)
                else:
                    l = 0
                    r = len(stack) - 1
                    while l<r:
                        mid = (l+r)//2
                        if stack[mid]<i:
                            l = mid + 1
                        else:
                            r = mid
                    stack[l] = i
        return len(stack)