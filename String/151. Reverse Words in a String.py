class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split()
        tmp = ' '.join(tmp[::-1])
        return tmp
