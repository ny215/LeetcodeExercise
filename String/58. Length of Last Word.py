class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        if not s:
            return 0
        lis = ' '.join(s.split())
        lis = lis.split(" ")
        return len(lis[-1])