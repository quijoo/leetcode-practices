# import heapq
# class Solution:
#     def nthUglyNumber(self, n):
#         if n == 1:
#             return 1
#         heap, dic, number, tmp = [1], {}, 0, 0
#         while number < n:
#             tmp = heapq.heappop(heap)
#             heapq.heappush(heap, tmp*2)
#             heapq.heappush(heap, tmp*3)
#             heapq.heappush(heap, tmp*5)
        
#             if tmp not in dic:
#                 number += 1
#                 dic[tmp] = 0
#         return tmp

# 由于数据范围较小， 可以预处理
# class Solution:
#     ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14))
#     def nthUglyNumber(self, n):
#         return self.ugly[n-1]


# dp 方法
class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]