class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        return self.dfs(sorted(nums), target, memo)
        print memo

    
    
    def dfs(self, nums, target, memo):
        if target in memo:
            return memo[target]
        count = 0        
        for num in nums:
            if num > target:
                break
            elif num == target:
                count += 1
                break
            else:
                count += self.dfs(nums, target - num, memo)
        memo[target] = count
        return count