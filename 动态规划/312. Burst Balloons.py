
# @functools.lru_cache

# @functools.lru_cache(maxsize=128, typed=False)
# New in version 3.2.
# Changed in version 3.3: Added the typed option.
# 这个装饰器实现了备忘的功能，是一项优化技术，把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。lru 是（least recently used）的缩写，即最近最少使用原则。表明缓存不会无限制增长，一段时间不用的缓存条目会被扔掉。
# 这个装饰器支持传入参数，还能有这种操作的？maxsize 是保存最近多少个调用的结果，最好设置为 2 的倍数，默认为 128。如果设置为 None 的话就相当于是 maxsize 为正无穷了。还有一个参数是 type，如果 type 设置为 true，即把不同参数类型得到的结果分开保存，如 f(3) 和 f(3.0) 会被区分开。

from prettyprinter import pprint
# 这个题目中学到了逆向思维
class Solution:
    def maxCoins(self, nums):
        # 为0的气球无论在什么时候被搓破都没有影响
        try:
            nums.remove([0])
        except:
            pass
        # 防止下标越界
        nums.append(1)
        # 初始化dp数组
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # 遍历开区间长度, 由于是开区间， 如果区间内有气球那么长度一定大于2
        for length in range(2, len(nums)+1):
            # 遍历开区间
            for i in range(-1, len(nums) - length):
                j = i + length
                for mid in range(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[mid] * nums[j] + dp[i][mid] + dp[mid][j])
        return dp[-1][-1]
if __name__ == "__main__":
    
    pprint(Solution().maxCoins([3,1,5,8]))