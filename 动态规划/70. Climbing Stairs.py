class Solution:
    def climbStairs(self, n):
        status = [0]*(n + 1)
        status[1] = 1
        status[2] = 1
        for i in range(2, n):
            status[i] = status[i-1] + status[i-2]
        print(status[-1])


if __name__ == "__main__":
    Solution().climbStairs(2)
            