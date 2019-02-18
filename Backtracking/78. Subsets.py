class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums,0,[], res)
        return res
    def dfs(self,nums, start, tmp, res):
        res.append(tmp[:]) #copy
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, i+1, tmp, res)
            tmp.pop()

            