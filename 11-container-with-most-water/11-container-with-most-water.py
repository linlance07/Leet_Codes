class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            H = min(height[l],height[r])
            dist = r - l
            ans = max(ans,H*dist)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return ans