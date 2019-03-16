class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = n-1
        while right-1 >= 0 and nums[right] <= nums[right-1]:
            right -= 1
        if right == 0:
            return self.reverse(nums,0,n-1)
        pivot = right -1
        successor = 0
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        self.reverse(nums, pivot+1, n-1)
    
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
#time: O(n)
#space: O(n)