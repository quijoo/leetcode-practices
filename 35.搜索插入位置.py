class Solution:
    def searchInsert(self, nums, target):
        return self.find(nums, 0, len(nums) - 1, target)
    def find(self, nums, i, j, target):
        print(nums[i:j+1])
        if i == j:
            return i+1 if nums[i] <= target else i
        mid = (i+j)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.find(nums, i, mid-1, target)
        elif nums[mid] < target:
            return self.find(nums, mid+1, j, target)


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,6]
    t = 2
    print(s.searchInsert(nums, t))