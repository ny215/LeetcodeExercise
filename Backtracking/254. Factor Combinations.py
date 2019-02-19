class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 2:
            return []

        res = []
        self.dfs(n,2,[],res)
        return res

    def dfs(self, n, start, tmp, res):
        if tmp and n > 1:
            res.append(tmp + [n]) 
        for i in range(start, int(math.sqrt(n))+1):
            if n % i == 0:
                tmp.append(i)
                self.dfs(n/i, i, tmp, res)
                tmp.pop()
                