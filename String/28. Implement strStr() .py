class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        n = len(needle)
        if n == 0:
            return 0
        left = 0
        right = left + n
        while left <= len(haystack) - n:
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1
        