class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(n,1, [], res, k)
        return res
        
    def dfs(self,n, start, tmp, res, k):
        if k == 0:
            res.append(tmp[:])
            return
        for i in range(start, n+1):
            tmp.append(i)
            self.dfs(n, i+1, tmp, res, k-1)
            tmp.pop()

       