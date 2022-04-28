class Solution:
    def exist(self, board, word):
        
        def dfs(i, j, k):
            nonlocal board
            nonlocal status
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k] or status[i][j] == 1: return False
            if k == len(word) - 1: return True
            # tmp, board[i][j] = board[i][j], '/'
            status[i][j] = 1
            r = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # board[i][j] = tmp
            status[i][j] = 0
            return r

        # 先查找到与word首字母相同的点， 然后开始搜索
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    status = [[0 for _ in range(len(board[0]))] for _ in range(len(board))] 
                    if dfs(x, y, 0):return True
        return False




