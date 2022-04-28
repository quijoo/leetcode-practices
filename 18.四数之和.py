class Solution:
    def fourSum(self, nums, target):
        # 排序
        nums.sort()
        size = len(nums)
        res = []
        dic = {}
        for a in range(0, size-3):
            for b in range(a+1, size-2):
                # if b < size-2:
                c = b + 1
                d = size -1
                while c < d:
                    while c < d and nums[c] + nums[a] + nums[b] + nums[d] > target:
                        d -= 1
                    if c<d  and nums[c] + nums[a] + nums[b] + nums[d] == target and (nums[a], nums[b], nums[c], nums[d]) not in dic:
                        dic[(nums[a],nums[b],nums[c],nums[d])] = 0
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
        return res



