class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = (right - left)*min(height[left], height[right])
        while left < right:
            if left < right and height[left] < height[right]:
                left += 1
                res = max(res, (right - left)*min(height[left], height[right]))
            elif left < right:
                right -= 1
                res = max(res, (right - left)*min(height[left], height[right]))
        return res