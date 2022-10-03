class Solution:
    def minCost(self, colors: str, time: List[int]) -> int:
        stack = []
        for i in range(len(colors)):
            if not stack:
                stack.append((colors[i],time[i]))
            else:
                if stack[-1][0]==colors[i]:
                    if stack[-1][1]<=time[i]:
                        stack.pop()
                        stack.append((colors[i],time[i]))
                else:
                    stack.append((colors[i],time[i]))
        s = sum(time)
        #print(stack)
        for i,j in stack:
            s -= j
        return s