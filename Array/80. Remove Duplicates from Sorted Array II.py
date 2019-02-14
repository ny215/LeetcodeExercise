class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        count = 2
        for num in nums[2:]:
            print nums
            if num != nums[count - 2]:
                nums[count] = num
                count += 1
        return count