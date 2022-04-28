# def partition(attr, left, right):
#     mid = attr[left]
#     while left < right:
#         # 这里的等于， 考虑到 attr[left] == attr[right] 的情况。 该情况下无论怎么交换都会卡在原地
#         # 更深层的考虑 我们划分的目的是 max(attr[:mid]) <= mid <= min(attr[mid+1:]) 而不是 max(attr[:mid]) < mid < min(attr[mid+1:])
#         # 我们不能保证 mid 在数组中不重复， 所以要将所有 >= mid的数放在右边数组， 所以是 while left < right and attr[right] >= mid:,否则就会出现上诉死循环的的表现情况 
#         while left < right and attr[right] >= mid:
#             right -= 1
#         attr[left] = attr[right]
#         while left < right and attr[left] <= mid:
#             left += 1
#         attr[right] = attr[left]
#     attr[left] = mid
#     return left

# def sort(attr, i, j):
#     if i >= j:
#         return
#     mid = partition(attr, i, j)
#     sort(attr, i, mid - 1)
#     sort(attr, mid + 1, j)







# def partiotion(attr, i, j):
#     mid = attr[i]
#     while i < j:
#         while i<j and attr[j] <= mid:
#             j -= 1
#         attr[i] = attr[j]
#         while i<j and attr[i] >= mid:
#             i += 1
#         attr[j] = attr[i]
#     attr[i] = mid
#     return i
# def sort(attr, i, j):
#     if i >= j:
#         return 
#     mid = partition(attr, i, j)
#     sort(attr, i, mid-1)
#     sort(attr, mid+1, j)





def partition(attr, left, right):
    mid = attr[left]
    while left < right:
        while left < right and attr[right] >= mid:
            right -= 1
        attr[left] = attr[right]
        while left < right and attr[left] <= mid:
            left += 1
        attr[right] = attr[left]
    attr[left] = mid
    return left

def sort(attr, left, right):
    if left >= right:
        return
    mid = partition(attr, left, right)
    sort(attr, left, mid-1)
    sort(attr, mid+1, right)




if __name__ == "__main__":
    l = [5,1,1,2,0,0]
    sort(l, 0, len(l) - 1)
    print(l)



