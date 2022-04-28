import heapq as hq
import math
# 理解
graph = {
    'A':{'B':5, 'C':1},
    'B':{'A':5, 'C':2, 'D':1},
    'C':{'A':1, 'B':2, 'D':4, 'E':8},
    'D':{'B':1, 'C':4, 'E':3, 'F':6},
    'E':{'C':8, 'D':3},
    'F':{'D':6},
}

def init_distance(graph, s):
    # 初始化距离数组
    distance = {s:0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance 
def dijkstra(graph, s):
    # 初始化
    pqueue = list()
    # 将初始节点放入队列
    hq.heappush(pqueue, (0, s))
    
    # 建立 seen 字典
    seen = set()
    
    # 用于得到最短路径的具体路径
    parent = {s:None}
    distance = init_distance(graph, s)

    # 每次取出一个距离 s 最近的节点
    while (len(pqueue) > 0):
        pair = hq.heappop(pqueue)
        dist, vertex = pair[0], pair[1]
        seen.add(s)

        nodes = graph[vertex].keys()
        for w in nodes:
            # 未被访问过
            if w not in seen:
                # 如果经过 vertex - w 比 经过旧的路到 w 更近
                if dist + graph[vertex][w] < distance[w]:
                    # 那么久更新为新的路
                    # 如果保证每次从队列里取出来的是距离 s 最近的节点
                    
                    hq.heappush(pqueue, (dist + graph[vertex][w], w))

                    # 记录到 w 最近的节点是 vertex
                    parent[w] = vertex
                    # 更新最近距离
                    distance[w] = dist + graph[vertex][w]
    return parent, distance
if __name__ == "__main__":
    print(dijkstra(graph, 'A'))


