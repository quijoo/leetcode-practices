import queue
import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        status = [0] * numCourses
        edges = collections.defaultdict(list)
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        valid = True
        q = []

        def dfs(u: int):
            nonlocal valid
            status[u] = 1
            for v in edges[u]:
                if status[v] == 1:
                    valid = False
                    return
                elif status[v] == 0:
                    dfs(v)
                    if not valid:
                        return 
            status[u] = 2
            q.append(u)


        for i in range(numCourses):
            if valid and status[i] == 0:
                dfs(i)
        if not valid:
            return []

        return q



class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        status = [0] * numCourses
        edges = collections.defaultdict(list)
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        valid = True
        def dfs(u: int):
            nonlocal valid
            status[u] = 1
            for v in edges[u]:
                if status[v] == 1:
                    valid = False
                    return
                elif status[v] == 0:
                    dfs(v)
                    if not valid:
                        return 
            status[u] = 2
            q.append(u)


        for i in range(numCourses):
            if valid and status[i] == 0:
                dfs(i)
        return valid
if __name__ == "__main__":
    print(Solution().findOrder(2, [[1,0]]))








































