class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res =[]
        self.dfs(k, n, 1, [], res)
        return res
    
    
    def dfs(self,k, n, start, tmp, res):
        if n == 0 and k == 0:
            res.append(tmp[:]) #shallow copy
            return
        if k == 0:
            return
        for i in range(start, 10): #check the range; read the question
            tmp.append(i)
            self.dfs(k-1, n-i, i+1, tmp, res)
            tmp.pop()
            