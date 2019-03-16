class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        res = []
        self.dfs(nums,[], res)
        return res
    
    def dfs(self, nums, tmp, res):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for i in xrange(len(nums)):
            if nums[i] in tmp:
                continue
            tmp.append(nums[i])
            self.dfs(nums, tmp, res)
            tmp.pop()