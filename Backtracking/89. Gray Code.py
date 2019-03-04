class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        max = 2**n
        for i in range(1,max):
            res.append(res[-1] ^( i& -i))
        return res
        