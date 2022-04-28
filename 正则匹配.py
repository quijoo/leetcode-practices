class Solution:
    def matches(self, s, p, i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
    
    def isMatch(self, s: str, p: str) -> bool:
        # 初 始 化 D P 数 组
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True

        # 遍 历 D P 矩 阵
        for i in range(m + 1):
            for j in range(1, n + 1):
                
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if self.matches(s, p, i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if self.matches   (s, p, i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]