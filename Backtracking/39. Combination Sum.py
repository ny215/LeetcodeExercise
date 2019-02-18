class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
        
        
    def dfs(self, candidates, target, start, tmp, res):
        if target < 0:      # backtracking
            return
        if target == 0:
            res.append(tmp[:])

        for i in range(start, len(candidates)):
            tmp.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, tmp, res)
            tmp.pop()

            
            
        