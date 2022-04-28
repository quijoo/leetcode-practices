#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        parent = [0]*numCourses
        edges = collections.defaultdict(list)
        status = [0]*numCourses
        # 现在是实现的是dfs版本
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        valid = True
        res = []
        def dfs(s):
            status[s] = 1
            nonlocal valid
            for i in edges[s]:
                if status[i] == 0:
                    dfs(i)
                    if not valid:
                        return
                elif status[i] == 1:
                    valid = False
            status[s] = 2
            res.append(s)

        for i in range(numCourses):
            if valid and status[i] == 0:
                dfs(i)
        res.reverse()
        return res if valid else []

        

# @lc code=end

