class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                cur = dp[j]
                if j == i:
                    dp[j] = tmp + triangle[i][j]
                elif not j:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(tmp, dp[j]) + triangle[i][j]
                tmp = cur
        return min(dp)