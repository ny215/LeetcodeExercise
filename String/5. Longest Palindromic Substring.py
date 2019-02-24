class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""
        res = ""
        start = end = 0
        for i in range(len(s)):
            checkOdd = self.expand(s, i, i+1)
            checkEven = self.expand(s, i, i)
            tmpmax = max(checkOdd, checkEven)
            if tmpmax > (end - start):
                start = i - int((tmpmax - 1) / 2)
                end = i + int(tmpmax / 2)
        return s[start:end+1]
            
            
    def expand(self, string, start, end):
        left = start
        right = end
        while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
        return right - left -1