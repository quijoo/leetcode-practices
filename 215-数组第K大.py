import random
class Solution:
    nums = []
    k = -1
    def findKthLargest(self, nums, k) :
        return self.func(nums, len(nums) - k)

    def func(self, nums, k):
        
        length = len(nums)
        if length == 1:
            return nums[0]
        middle = nums[length//2]
        start = 0
        end = length - 1
        while (start <= end):
            if nums[start] < middle:
                start += 1
            else:
                end -= 1
                nums[start], nums[end] = nums[end], nums[start]
        
        
        print(nums[:start+1], nums[end:], start, end, k)
            
        if nums == self.nums and k == self.k:
            return nums[k]
        else:
            self.nums = nums
            self.k = k

        print(nums[:start+1], nums[end:], start, end, k)

        if k <= start:
            return self.func(nums[:start+1], k)
            
        elif k >= end:
            return self.func(nums[end:], k-end)


if __name__ == "__main__":
    s = Solution()
    l = [random.randint(0,10) for x in range(0, 6)]
    print(l)
    print(s.findKthLargest(l, 2))
