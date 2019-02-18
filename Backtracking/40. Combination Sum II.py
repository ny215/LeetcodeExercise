class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
    
    def dfs(self, candidates, target, start, tmp, res):
        if target == 0:
            res.append(tmp[:])
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if not(i > start and candidates[i-1] == candidates[i]):
                tmp.append(candidates[i])
                self.dfs(candidates, target - candidates[i], i+1, tmp, res)
                tmp.pop()