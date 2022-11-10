class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack += [i]
            else:
                if stack[-1]==i:
                    stack.pop()
                else:
                    stack += [i]
        return "".join(stack)