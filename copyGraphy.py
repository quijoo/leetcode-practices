
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        if not node:return
        clone = Node(node.val, [])
        dic = {}
        def dfs(node):
            if node in dic:
                return dic[node]
            tmp = Node(node.val, [])
            dic[node] = tmp
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)        
