class Solution:
    def find(self, i, j):
        mid = (i+j)//2
        if isinstance(mid) and not isinstance(mid-1):
            return mid+1
        if isinstance(mid):
            return self.find(i, mid-1)
        else:
            return self.find(mid+1, j)
    def firstBadVersion(self, n):
        return self.find(1, n)
        