class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """  
        k = k % len(nums)  #k could be larger than len(nums)
        self.helper(nums, 0, len(nums)-1) #rotate the whole list
        self.helper(nums,0, k-1)   #rotate first part
        self.helper(nums, k, len(nums)-1) #rotate the last part

    def helper(self, nums, left, right):
        while right > left:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    