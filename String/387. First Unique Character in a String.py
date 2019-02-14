class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res =[]
        dic ="abcdefghijklmnopqrstuvwxyz"
        for letter in dic:
            if s.count(letter) == 1:
                res.append(s.index(letter))
        if len(res) > 0:
            return min(res)
        else:
            return -1

    
        