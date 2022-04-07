class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            l = 0
            r = cols - 1
            while l<=r:
                mid = (l+r)//2
                if grid[i][mid]>=0:
                    l = mid + 1
                else:
                    r = mid - 1
            ans += (cols - l)
        return ans