# Python 3.6 后哈希表是有序的
class Solution:
    def firstUniqChar(self, s):
        if not s:
            return " "
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for key, val in d.items():
            if val == 1:
                return key
        return " "