class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums),0,[],res)
        return res
        
    def dfs(self, nums, start, tmp, res):
        res.append(tmp[:])        
        for i in range(start, len(nums)):
            if not (i > start and nums[i-1] == nums[i]):
                tmp.append(nums[i])
                self.dfs(nums, i+1, tmp, res)
                tmp.pop()
    