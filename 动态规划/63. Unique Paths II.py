# Unsolved
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        #dp = [[0] * n] * m    和上一行的区别为这一行实际上是浅拷贝。非常不安全。
        i = j = 0
        while i < m and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
                i += 1
        while j < n and obstacleGrid[0][j] == 0:
                dp[0][j] = 1
                j += 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]