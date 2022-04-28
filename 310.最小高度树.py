#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
# 思路：删掉 degree == 1 的节点
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return edges[0] 
        degree= [0]*n
        dic = collections.defaultdict(list)
        # 初始化度数 和 边
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        while len(dic) > 2:
            tmp = []
            for i in range(n):
                if degree[i] == 1:
                    tmp.append(i)
            for i in tmp:
                parent = dic.pop(i)[0]
                dic[parent].remove(i)
                degree[parent] -= 1
                degree[i] = 0
        return list(dic.keys())
# @lc code=end

