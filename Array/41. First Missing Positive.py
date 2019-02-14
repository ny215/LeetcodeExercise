class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1
        n = len(nums)
        if n == 1:
            return 2
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):  
            a = abs(nums[i])  # have to use abs because it may change to negative
            
            if a == n:  #use first place to track n, as we've checked if 1 is in the list. Then flip the sign
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
                
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        # n is not in the list
        if nums[0] > 0:
            return n
        
        
        #every number <=n is in the list, return the next larger one
        return n + 1
            
            
    

        