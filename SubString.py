class Solution:
    def longestPalindrome(self, s):
        if s == "" or len(s) == 1:
            return s
        elif len(s)==2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        tmp = ''
        for ch in s:
            tmp += ch + '#'
        tmp = tmp[:-1]
        val = (0, -1, -1)
        for i in range(1, len(tmp) - 1):
            left = i-1
            right = i+1
            
            lens = 0 if tmp[i] == '#' else 1
            while (left >= 0 and right <= len(tmp) -1) and tmp[left] == tmp[right]:
                if tmp[left] != '#':
                    lens += 2
                left -= 1
                right += 1
            if lens > val[0]:
                val = (lens, left + 1, right - 1)
        res = ""
        for c in tmp[val[1]:val[2]+1]:
            if c != '#':
                res += c
        return res
if __name__ == "__main__":
    print(Solution().longestPalindrome("32356"))