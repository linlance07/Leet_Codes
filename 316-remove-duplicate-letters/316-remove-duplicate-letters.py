class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        D = Counter(s)
        stack = []
        visit = set()
        for i in range(len(s)):
            if s[i] in visit:
                D[s[i]] -= 1
                continue
            while stack and stack[-1]>s[i] and D.get(stack[-1],0)>1:
                D[stack[-1]] -= 1
                #stack.pop()
                visit.remove(stack.pop())
            visit.add(s[i])
            stack.append(s[i])

        return "".join(stack)