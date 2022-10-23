class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ind = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and stack[-1]==popped[ind]:
                stack.pop()
                ind += 1
        while stack:
            while stack and stack[-1]==popped[ind]:
                stack.pop()
                ind += 1
            else:
                return False
        return True