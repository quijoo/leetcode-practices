from prettyprinter import pprint
class Solution:
    def numIslands(self, grid):
        def dfs(i, j):
            nonlocal grid
            if i < 0 or i >3 or j > 4 or j <0:
                return
            elif grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)
        num = 0
        for i in range(4):
            for j in range(5):
                if grid[i][j] != '0':
                    num += 1
                    _ = dfs(i, j)

        return num
if __name__ == "__main__":
    print(Solution().numIslands([
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
        ]))

            

