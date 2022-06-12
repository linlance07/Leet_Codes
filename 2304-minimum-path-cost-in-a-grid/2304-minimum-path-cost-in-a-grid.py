class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        C = defaultdict(list)
        for i in range(len(moveCost)):
            C[i] += moveCost[i]
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        mini = float('inf')
        for i in range(len(grid[0])):
            dp[0][i] = grid[0][i]
        for j in range(1,len(grid)):
            for k in range(len(grid[0])):
                for __ in range(len(grid[0])):
                    mini = min(mini,dp[j-1][__]+C[grid[j-1][__]][k])
                    dp[j][k] = min(dp[j][k],mini+grid[j][k])
                    mini = float('inf')
        return min(dp[-1])
                
                
        
        
        
        
        