class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i,j in enumerate(s):
            if j=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    ans = max(ans,i-stack[-1])
                else:
                    stack.append(i)
        return ans
                    
            