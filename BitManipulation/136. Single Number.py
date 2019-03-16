class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res
    
#bit manipulation
# time: O(n)
# space: O(1)