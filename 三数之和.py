class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        for a in range(0, size):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b = a + 1
            c = size - 1
            while b < c:
                while b < c and nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                if b < c and nums[a] + nums[b] + nums[c] == 0:
                    res.append([nums[a], nums[b], nums[c]])
                while b < c and nums[b] == nums[b+1]:
                    b += 1
                b += 1
        return res