class Solution:
    def maxsublist(self, array):
        res = tmp = array[0]
        for i in array[1:]:
            tmp = max(i, tmp + i)
            res = max(res, tmp)
        return res


if __name__ == "__main__":
    print(Solution().maxsublist([43,5,2,1,3,-32, 41,4]))