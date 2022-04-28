
class Solution:
    def maxValue(self, grid):
        if not grid:
            return 0
        if not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]