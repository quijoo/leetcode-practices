#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 创建初始集合
        # 2. collection 是安全的集合， 访问不存在的点也不会有问题
        edges = collections.defaultdict(list)

        # 3. 记录每个点的入度
        indeg = [0] * numCourses

        # 4. 构建邻接表和入度
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        # 5. 将入度为 0 的点入队列
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        
        # 被访问的点的数量
        visited = 0

        # 从队列中取数字
        while q:
            # 访问一个节点
            visited += 1
            u = q.popleft()

            # 访问该节点的所有后继节点， 并将它们的入度 - 1
            for v in edges[u]:
                indeg[v] -= 1
                # 如果是去掉该边后入度为0那么久可以修该门课
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses
# @lc code=end



