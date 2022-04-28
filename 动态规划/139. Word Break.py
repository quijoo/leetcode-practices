class Solution:
    def wordBreak(self, s, wordDict):
        dic = {}
        for word in wordDict:
            dic[word] = 0
        dp = [False for _ in range(len(s))]
        
        for i in range(len(s)):

            for j in range(i):
                dp[i] = dp[i] or (dp[j] and (s[j+1:i+1] in dic))
               
        return dp[-1]