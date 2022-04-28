import time
import random
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        sorted_ = True
        for j in range(len(nums) - i - 1):    
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                sorted_ = False
        if sorted_:
            break
    return nums

def select_sort(nums):
    
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

def sort_test(func, *args):
    t = time.time()
    tmp = func(*args)
    print("Spend Time:{}".format(time.time() - t))
    # print(tmp[:20])


def qsort(nums, i, j):
    def partition(nums, left, right):
        mid = nums[left]
        while left < right:
            while left < right and mid <= nums[right]:
                right -= 1
            nums[left] = nums[right]
            while left < right and mid >= nums[right]:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        return left
    if i >= j:
        return
    middle = partition(nums, i, j)
    qsort(nums, i, middle - 1)
    qsort(nums, middle+1, j)


def merge_sort(nums):
    def merge(a, b):
        tmp, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(b[j])
                j += 1
        if i == len(a):
            for x in b[j:]:
                tmp.append(x)
        else:
            for x in a[i:]:
                tmp.append(x)
        return tmp
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

    


if __name__ == "__main__":
    unsorted = list(range(1000000))
    random.shuffle(unsorted)
    # 显然选择排序更快
    sort_test(qsort, unsorted, 0, len(unsorted)-1)
    sort_test(merge_sort, unsorted)
    sort_test(bubble_sort, unsorted)
    sort_test(select_sort, unsorted)
    