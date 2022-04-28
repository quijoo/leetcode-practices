import math
class Solution:
    def coinChange(self, coins, amount):
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        try:
            coins.remove(0)
        except:
            pass
        for i in range(min(coins), amount+1):
            for coin in coins:
                if coin <= amount:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != math.inf else -1


if __name__ == "__main__":
    Solution().coinChange([1,2,34],100)