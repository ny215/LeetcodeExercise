class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        n = len(nums)

        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            print l, r

        right = r
        
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
            print l, r
        left = l
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]