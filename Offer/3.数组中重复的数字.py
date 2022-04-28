class Solution():
    def duplicateInArray(self, nums):
        fast = slow = 0

        # 初始时 f == 0， 结束时 f == s
        while fast == 0 or fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        return slow
