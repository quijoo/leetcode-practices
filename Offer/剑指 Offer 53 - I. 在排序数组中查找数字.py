class Solution:
    def search(self, nums: [int], target: int) -> int:
        # right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        if j >= 0 and nums[j] != target: 
            return 0
        i = 0
        # left
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1


from functools import *
@lru_cache()