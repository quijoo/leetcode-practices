# heappush 将 item 添加进 heap 
# heapq.heappush(heap, item)
# Push the value item onto the heap, maintaining the heap invariant.

#  pop and return
# heapq.heappop(heap)
# Pop and return the smallest item from the heap, maintaining the heap invariant. 
# If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].


# push and pop
# heapq.heappushpop(heap, item)
# Push item on the heap, then pop and return the smallest item from the heap.
# The combined action runs more efficiently than heappush() followed by a separate call to heappop().

# 线性时间内 将 x 转化为 heap 
# heapq.heapify(x)
# Transform list x into a heap, in-place, in linear time.

# pop and return
# heapq.heapreplace(heap, item)
# Pop and return the smallest item from the heap, and also push the new item. 
# The heap size doesn’t change. If the heap is empty, IndexError is raised.

# 不清楚是什么作用
# heapq.merge(*iterables)
# Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). 
# Returns an iterator over the sorted values.


# 返回前 N 大
# heapq.nlargest(n, iterable[, key])
# Return a list with the n largest elements from the dataset defined by iterable. 
# key, if provided, specifies a function of one argument that is used to
# extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]

# 返回 N 小
# heapq.nsmallest(n, iterable[, key])
# Return a list with the n smallest elements from the dataset defined by iterable. key, 
# if provided, specifies a function of one argument that is used to 
# extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key)[:n]


class MaxHeap(object):
 
    def __init__(self):
        self._data = []
        self._count = len(self._data)
 
    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0
 
    def add(self, item):
        # 插入元素入堆
        if self._count >= len(self._data):
            self._data.append(item)
        else:
            self._data[self._count] = item
 
        self._count += 1
        self._shiftup(self._count-1)
 
    def pop(self):
        # 出堆
        if self._count > 0:
            ret = self._data[0]
            # 将最后一个元素放到堆顶， 这里可以用 pop
            self._data[0] = self._data[self._count-1]
            self._count -= 1
            self._shiftDown(0)
            return ret
        
    def _shiftup(self, index):
        # 上移self._data[index]，以使它不大于父节点
        parent = (index-1)>>1
        while index > 0 and self._data[parent] < self._data[index]:
            # swap
            self._data[parent], self._data[index] = self._data[index], self._data[parent]
            index = parent
            parent = (index-1)>>1
 
    def _shiftDown(self, index):
        # 上移self._data[index]，以使它不小于子节点
        j = (index << 1) + 1
        while j < self._count :
            # 有子节点
            if j+1 < self._count and self._data[j+1] > self._data[j]:
                # 有右子节点，并且右子节点较大
                j += 1
            if self._data[index] >= self._data[j]:
                # 堆的索引位置已经大于两个子节点，不需要交换了
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j
            j = (index << 1) + 1







import heapq

class Solution():
    def nlargest(self, li, k):
        return heapq.nlargest(li, k)


if __name__ == "__main__":
    print(Solution().nlargest(3, [11,22,3,4,32,32,432,3,213]))


