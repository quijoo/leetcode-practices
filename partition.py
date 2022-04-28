
import random

class Solution:
    def findKthLargest(self, nums, k):
        return self.maxN(nums, len(nums) - k)

    def partition(self, l):
        left = 0
        right = len(l) - 1
        solt = l[right]
        while(left < right):
            if l[left] < solt:
                left += 1
            else:
                l[right] = l[left]
                right -= 1
                l[left] = l[right]
        l[right] = solt
        return l, right

    def maxN(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        nums, mid = self.partition(nums)
        if mid == k:
            return nums[k]
        elif k < mid:
            return self.maxN(nums[:mid], k)
        else:
            return self.maxN(nums[mid+1:], k-(mid+1))




if __name__ == "__main__":
    s = Solution()
    l = [10,9,8,7,6,5]
    k = 3
    print(s.findKthLargest(l, k))
    