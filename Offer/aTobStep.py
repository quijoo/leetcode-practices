# # import math
# # def optiStep(s, e):
# #     res = 0
# #     while s ^ e > s:
# #         res += (e & 1) + 1
# #         e >>= 1
# #     return res + abs(e-s)


# # def solve(s, e):
# #     num = 0
# #     while 2*s < e:
# #         if not e % 2:
# #             e /= 2
# #             num += 1
# #         else:
# #             if not ((e + 1) / 2) % 2:
# #                 e = (e+1)/2
# #             else:
# #                 e = (e - 1)/2
# #             num += 2
# #     num += min(e-s, s - e / 2 + 1, s - (e - 1)/2 + 2,s - (e + 1)/2 + 2)
# #     return num
    
    




# # import queue
# # def compute(s, e):
# #     q = queue.Queue()
# #     q.put(s)
# #     n = 0
# #     while not q.empty():
# #         tmp = []
# #         while not q.empty():
# #             val = q.get()
# #             if val == e:
# #                 return n
# #             tmp.append(val)
# #         for item in tmp:
# #             q.put(item - 1)
# #             q.put(item + 1)
# #             q.put(item * 2)
# #         n += 1


# # for s in range(1, 16):
# #     for e in range(1, 16):
# #         if s < e :
# #             r1, r2 = compute(s, e), optiStep(s,e)
# #             if not r1 == r2:
# #                 print(bin(s), bin(e), r1, r2, r1==r2)



# # a + b + c = 0
# # 方法一：哈希表存 -x 然后暴力 + 去重
# # 方法二： 枚举 c， 双指针搜索 a，b ， 不用去重
# import copy
# def printlist(li):
#     for l in li:
#         print(str(l).replace(",", " ").replace("[","").replace("]", ""))
# def treeTuple(nums):

#     recod = {}
#     repeat = {}
#     res = []
#     for x in range(len(nums)):
#         if -nums[x] not in recod:
#             recod[-nums[x]] = [x]
#         else:
#             recod[-nums[x]].append(x)


#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] in recod:
#                 tlist = copy.deepcopy(recod[nums[i] + nums[j]])
#                 try:
#                     tlist.remove(i)
                    
#                 except:
#                     pass
#                 try:
#                     tlist.remove(j)
#                 except:
#                     pass
#                 if tlist:
#                     tt = [nums[i], nums[j], - nums[i] - nums[j]]
#                     tt.sort()
#                     tmp = str(tt).replace(",", " ").replace("[","").replace("]", "")
#                     if tmp not in repeat:
#                         res.append(tt)
#                         repeat[tmp] = 1
#     res.sort()
#     return res

# if __name__ == "__main__":

#         s = list(map(lambda x:int(x), input().split(" ")))

#         printlist(treeTuple(s))

    
# def fibangle(n):
#     if n == 0:
#         return 
#     elif n == 1:
#         print(1)
#         return
#     elif n == 2:
#         print(1)
#         print('1 1 1')
#         return
#     print(1)
#     print('1 1 1')
#     a = b = 1
#     fib = [1,1]
#     for i in range(2, n):
#         fib.append(a + b)
#         a, b = b, fib[-1]
        
#         print(str(fib + fib[:len(fib)-1][::-1]).replace(",", "").replace("]", "").replace("[", ""))
# if __name__ == "__main__":
#     n = int(input())
#     fibangle(n)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.visited = False





class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.visited = False

def solve(li, n1, n2):
    # li = [3, 5 ,6, -1 ,-1 ,2 ,7 ,-1 ,-1, 4 ,-1 ,-1 ,1 ,9 ,-1 ,-1, 8 ,-1, -1]
    def build():
        nonlocal li
        val = li[0]
        li.pop(0)
        root = Node(val)
        if val == -1:
            return root
        root.left = build()
        root.right = build()
        return root
    r = build()
    def lowestCommonAncestor(root, A, B):

        if(root is None or root.val==A or root.val==B):
            return root
        left=lowestCommonAncestor(root.left,A,B)
        right=lowestCommonAncestor(root.right,A,B)
        if left and right :
            return root
        return left or right
    node = lowestCommonAncestor(r, n1, n2)
    print(node.val)



if __name__ == "__main__":
    li = list(map(lambda x:int(x), input().split(" ")))
    l2 = list(map(lambda x:int(x), input().split(" ")))
    solve(li, l2[0], l2[1])






#include <stdio.h>
#include <math.h>

float f(float x, float y, float z) {
    float a = x * x + 9.0f / 4.0f * y * y + z * z - 1;
    return a * a * a - x * x * z * z * z - 9.0f / 80.0f * y * y * z * z * z;
}

float h(float x, float z) {
    for (float y = 1.0f; y >= 0.0f; y -= 0.001f)
        if (f(x, y, z) <= 0.0f)
            return y;
    return 0.0f;
}

int main() {
    for (float z = 1.5f; z > -1.5f; z -= 0.05f) {
        for (float x = -1.5f; x < 1.5f; x += 0.025f) {
            float v = f(x, 0.0f, z);
            if (v <= 0.0f) {
                float y0 = h(x, z);
                float ny = 0.01f;
                float nx = h(x + ny, z) - y0;
                float nz = h(x, z + ny) - y0;
                float nd = 1.0f / sqrtf(nx * nx + ny * ny + nz * nz);
                float d = (nx + ny - nz) * nd * 0.5f + 0.5f;
                putchar(".:-=+*#%@"[(int)(d * 5.0f)]);
            }
            else
                putchar(' ');
        }
        putchar('\n');
    }
}