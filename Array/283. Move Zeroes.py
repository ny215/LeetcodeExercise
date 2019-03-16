class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        ind = 0
        for i in range(n):
            if nums[i] == 0:
                continue
            nums[ind]  = nums[i]
            ind += 1
        for j in range(ind,n):
            nums[j] = 0
            
#time: O(n)
#space: O(1)
                