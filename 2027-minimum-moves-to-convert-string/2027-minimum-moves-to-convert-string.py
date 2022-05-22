class Solution:
    def minimumMoves(self, s: str) -> int:
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i]=='X':
                if stack:
                    stack.append(s[i])
                    if len(stack)==3:
                        stack = []
                        ans += 1
                else:
                    stack.append(s[i])
            else:
                if stack:
                    stack.append(s[i])
                    if len(stack)==3:
                        stack = []
                        ans += 1
        if stack:
            ans += 1
        return ans
                    
            
            