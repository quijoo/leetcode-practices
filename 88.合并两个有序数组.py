class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = m + n - 1
        pos = n - 1
        while pos >= 0:
            if p1 < 0:
                nums1[p2] = nums2[pos]
                pos -= 1
            elif nums1[p1] < nums2[pos]:
                nums1[p2] = nums2[pos]
                pos -= 1
            else:
                nums1[p2] = nums1[p1]
                p1 -= 1
            p2 -= 1
        return nums1
