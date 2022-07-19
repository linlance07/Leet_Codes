class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights += 0,
        for i in range(len(heights)):
            while stack and stack[-1][1]>=heights[i]:
                H = stack.pop()[1]
                W = i if not stack else i-stack[-1][0]-1
                ans = max(ans,H*W)
            stack.append((i,heights[i]))
        return ans