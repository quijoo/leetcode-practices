import math
class Solution:
    def numSquares(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        squares = [i**2 for i in range(1, int(round(math.sqrt(n))) + 1)]
        for i in range(1, n+1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        return dp[-1]

