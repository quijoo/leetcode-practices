# 以字典实现图
# {"Node":[]}
import queue
class Graph:
    def __init__(self, data = None):
        self.data = data
        self.len = len(list(data.keys()))
    def adjacent(self, x, y):
        return y in self.data[x]
    def neighbors(self, x):
        if x in self.data:
            # return list(map(lambda i:(x, i), self.data[x]))
            return data[x]
    def delVertex(self, x):
        self.data.pop(x)
        for link in self.data.keys():
            link.remove(x)
    def addEdge(self, x, y):
        if y not in self.data[x]:
            self.data[x].append(y)
    def removeEdge(self, x, y):
        if y in self.data[x]:
            self.data[x].remove(y)
    def firstNeighbor(self, x):
        return self.data[x][0]
    def nextNeighbor(self, x, y):
        if y in self.data[x]:
            return self.data[self.data.index(y)+1]
        else:
            return -1
 



def BFS(G, v):
    q = queue.Queue()
    visited = [False]*(G.len+1)
    print(v)
    visited[v] = True
    q.put(v)
    while not q.empty():
        v = q.get()
        for d in G.neighbors(v):
            if not visited[d]:
                print(d)
                visited[d] = True
                q.put(d)

def BFSMintrace(G, v):
    q = queue.Queue()
    visited = [False]*(G.len+1)
    distance = [-1]*((G.len+1))
    distance[v] = 0
    visited[v] = True
    q.put(v)

    while not q.empty():
        v = q.get()
        for d in G.neighbors(v):
            if not visited[d]:

                distance[d] = distance[v] + 1
                visited[d] = True
                q.put(d)
    return distance[1:]

  

def DFS(G, v, visited):
    print(v)
    visited[v] = True
    for k in G.neighbors(v):
        if not visited[k]:
            DFS(G, k, visited)
if __name__ == "__main__":
    data = {
        1:[2],
        2:[1,3,4],
        3:[2,4,5],
        4:[2,3,5,6],
        5:[3,4],
        6:[4,7],
        7:[6],
    }
    G = Graph(data)
    visited = [False]*(G.len+1)
    BFS(G, 1)
    print(BFSMintrace(G, 4))
    DFS(G, 1, visited)

    





