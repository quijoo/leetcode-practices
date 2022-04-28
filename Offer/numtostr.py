class Solution:
    def translateNum(self, num):
        dp = [0]*len(str(num))
        dp[0], dp[-1] = 1, 1
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i-1:i+1]) >= 26 or s[i-1] == '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]

class Solution:
    def translateNum(self, num):
        tmp1, tmp2 = 1, 1
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i-1:i+1]) >= 26 or s[i-1] == '0':
                tmp2, tmp1 = tmp2, tmp2
            else:
                tmp2, tmp1 = tmp1 + tmp2, tmp2
        return tmp2