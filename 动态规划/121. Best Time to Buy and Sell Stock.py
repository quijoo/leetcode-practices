import math
# 遍历数组考虑如果是当天卖出， 那么一定是在当天前的最低价格时买入是最赚的


# 两种方法分别是正序和逆序

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
        