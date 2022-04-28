# 统计每一个位的1出现的次数
# 例如 2301 如果该位是0， 那么 1 出现的次数就是 2219 那么1出现次数就是 229 + 1
#  该位 是 1 那么就是 hight * digital + low
# 该位是 2- 9  那么就是 （hitht+1）*digital




class Solution:
    def countDigitOne(self, n):
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            # cur不是最高位
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res