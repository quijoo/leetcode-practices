from heapq import *

class Solution():
    
    def __init__(self):
        self.heap = [], []
    
    def insert(self, num):
        small, large = self.heap
        # heapq 默认的是最小堆
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))
    
    def getMedian(self):
        small, large = self.heap
        if len(large) > len(small):
            return float(large[0])
        else:
            return (large[0] - small[0])/2.0

if __name__ == "__main__":
    tmp = []
    heap = Solution()
    for i in range(10):
        tmp.append(i)
        heap.insert(i)
        print(tmp, heap.getMedian())


