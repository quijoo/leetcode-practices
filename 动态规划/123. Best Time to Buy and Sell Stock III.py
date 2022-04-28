# class Solution:
#     def maxProfit(self, prices):
#         tmp = (math.inf, 0)
#         for sell in price:
#             tmp = (min(sell, lowest), max(prof, sell - price))
#         return tmp[1]


# class Solution:
#     def maxProfit(self, prices):
#         tmp = (0, 0)
#         prices.reverse()
#         for sell in prices:
#             tmp = (max(sell, tmp[0]), max(tmp[1], tmp[0] - sell))
#         return tmp[1]

import math
class Solution:
    def maxProfit(self, prices):

        right_tmp = [(0, 0)]*len(prices)
        for i in range(1, len(prices)):
            right_tmp[0 - i - 1] = (max(prices[0 - i - 1], right_tmp[0 - i][0]), max(right_tmp[0-i][1], right_tmp[0-i][0] - prices[0 - i - 1]))



        res = 0
        left_tmp = (prices[0], 0)
        for pos in range(2, len(prices) - 1):
            left_tmp = (min(prices[pos-1], left_tmp[0]), max(left_tmp[1], prices[pos-1] - left_tmp[0]))
            res = max(left_tmp[1] + right_tmp[pos])
        return res
