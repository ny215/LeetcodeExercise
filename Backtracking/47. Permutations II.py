class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        used = [False] * len(nums)
        self.dfs(sorted(nums), res, [], used)
        return res
    
    def dfs(self, nums, res, tmp, used):
        if len(tmp) == len(nums):
            res.append(tmp[:])
        for i in xrange(len(nums)):
            if used[i]:
                continue
            if nums[i] == nums[i-1] and i >0 and used[i-1]:
                continue
            used[i] = True
            tmp.append(nums[i])
            self.dfs(nums, res, tmp, used)
            used[i] = False
            tmp.pop()