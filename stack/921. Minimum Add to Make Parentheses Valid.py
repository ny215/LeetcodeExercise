class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        bal = 0
        for s in S:
            if s == "(":
                bal += 1
            elif s == ")":
                bal -= 1
            if bal == -1:
                res += 1
                bal += 1
        res = res + bal
        return res
# time: O(n)
#space: O(1)