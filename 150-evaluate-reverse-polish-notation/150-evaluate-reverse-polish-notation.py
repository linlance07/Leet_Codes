class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i[-1].isdigit():
                stack.append(int(i))
            else:
                b = stack.pop()
                if stack:
                    a = stack.pop()
                if i=='/':
                    stack.append(int(a/b))
                elif i=='*':
                    stack.append(a*b)
                elif i=='+':
                    stack.append(a+b)
                else:
                    stack.append(a-b)
        return stack[-1]